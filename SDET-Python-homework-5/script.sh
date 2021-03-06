#!/usr/bin/bash
if [[ -f answer.txt ]]; then
rm answer.txt
fi
echo 'Общее количество запросов' >> answer.txt
awk 'END { print NR }' access.log >> answer.txt

echo >> answer.txt

echo 'Общее количество запросов по типу' >> answer.txt

awk '{split($6,a, "\""); print a[2]}' access.log | sort | uniq -c >> answer.txt

echo >> answer.txt

echo '10 Самых частых запросов' >> answer.txt
grep -Po 'http?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)' access.log | sort | uniq -c | sort -nr | head >> answer.txt

echo >> answer.txt

echo 'Топ 5 самых больших запросов, которые завершились 4ХХ ошибкой' >> answer.txt
grep -Po '([\d\.]+) - - \[(.*?)] "(.*?)" (4\d\d) (\d+)' access.log | sort -n -r -k10 | head -5 | awk '{print $7, $9, $10, $1}' >> answer.txt

echo >> answer.txt

echo 'Топ 5 пользователей по количеству запросов, которые завершились 5ХХ ошибкой' >> answer.txt
grep -Po '([\d\.]+) - - \[(.*?)] "(.*?)" (5\d\d) (\d+)' access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -5 >> answer.txt
