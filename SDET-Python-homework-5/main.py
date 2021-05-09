import argparse
import json
import os
import re
from collections import Counter
from typing import Optional
from typing import Sequence

PATH_TO_ACCESS_LOG = 'access.log'


def count_lines(filename=PATH_TO_ACCESS_LOG):
    with open(filename) as f:
        return sum(1 for line in f if line.strip())


def count_by_methods(filename=PATH_TO_ACCESS_LOG):
    pattern = re.compile(r'(GET|POST|PUT|DELETE|UPDATE|PATCH|HEAD|CONNECT|OPTIONS|TRACE)')
    with open(filename) as f:
        for line in f:
            s = re.search(pattern, line.split(" ")[5])
            if s:
                yield s.group()


def top10(filename=PATH_TO_ACCESS_LOG):
    pattern = re.compile(
        r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)"
        r"(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+"
        r"(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
    with open(filename) as f:
        for line in f:
            s = re.search(pattern, line)
            if s:
                yield s.group()


def top5_by_bytes(filename=PATH_TO_ACCESS_LOG):
    pattern = re.compile(r'([(\d\.)]+) - - \[(.*?)] "(.*?)" (4\d\d) (\d+)')
    answer = []
    with open(filename) as f:
        for line in f:
            g = re.match(pattern, line)
            if g:
                g = g.groups()
                url = g[2].split(' ')[1]
                status = g[3]
                weight = g[-1]
                ip = g[0]
                answer.append((url, status, weight, ip))
    return list(sorted(answer, key=lambda x: int(x[2]), reverse=True))[:5]


def top5_by_5xx(filename=PATH_TO_ACCESS_LOG):
    pattern = re.compile(r'([(\d\.)]+) - - \[.*?] ".*?" 5\d\d \d+')
    with open(filename) as f:
        for line in f:
            g = re.match(pattern, line)
            if g:
                yield g.groups()[0]


def save(filename, text, data):
    with open(filename, 'a') as f:
        f.write(text + '\n')
        f.writelines(data)
        f.write('\n\n')


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('filename', help='Файл, для сохранения результатов')
    parser.add_argument('-c', '--count', action='store_true', help='Общее количество запросов')
    parser.add_argument('-ct', '--count_type', action='store_true', help='Общее количество запросов по типу')
    parser.add_argument('-mc', '--most_common', action='store_true', help='Топ 10 самых частых запросов')
    parser.add_argument('-mw', '--most_weight', action='store_true', help='Топ 5 самых больших по размеру запросов,'
                                                                          'которые завершились клиентской ошибкой')
    parser.add_argument('-se', '--server_error', action='store_true',
                        help='Топ 5 ip, которые завершились серверной 5ХХ ошибкой')
    parser.add_argument('--json', action='store_true', help='Сохранить собранные данные в JSON')
    args = vars(parser.parse_args(argv))

    filename = args['filename']
    if os.path.exists(filename):
        os.remove(filename)

    answer_json = {}

    if args['count']:
        text = 'Общее количество запросов'
        data = str(count_lines())
        if args['json']:
            answer_json[text] = data
        else:
            save(filename, text, [data])
    if args['count_type']:
        text = 'Общее количество запросов по типу'
        data = Counter(count_by_methods())
        if args['json']:
            answer_json[text] = [{'method': i, 'count': v} for i, v in data.items()]
        else:
            save(filename, text, [' '.join([i, str(v)]) + '\n' for i, v in data.items()])
    if args['most_common']:
        text = '10 самых частых запросов'
        data = Counter(top10()).most_common(10)
        if args['json']:
            answer_json[text] = [{'url': i[0], 'count': i[1]} for i in data]
        else:
            save(filename, text, [' '.join(map(str, i)) + '\n' for i in data])
    if args['most_weight']:
        text = 'Топ 5 самых больших запросов, которые завершились 4ХХ ошибкой'
        data = top5_by_bytes()
        if args['json']:
            answer_json[text] = [{'url': i[0], 'status_code': i[1], 'weight': i[2], 'ip': i[3]} for i in data]
        else:
            save(filename, text, [' '.join(map(str, i)) + '\n' for i in data])
    if args['server_error']:
        text = 'Топ 5 пользователей по количеству запросов, которые завершились 5ХХ ошибкой'
        data = Counter(top5_by_5xx()).most_common(5)
        if args['json']:
            answer_json[text] = [{'ip': i[0], 'count': i[1]} for i in data]
        else:
            save(filename, text, [' '.join(map(str, i)) + '\n' for i in data])

    if args['json']:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(answer_json, f, ensure_ascii=False, indent=4)

    return 0


if __name__ == '__main__':
    exit(main())
