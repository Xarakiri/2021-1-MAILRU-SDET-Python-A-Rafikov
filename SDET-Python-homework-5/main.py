import argparse
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
            s = re.search(pattern, line)
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


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--count', action='store_true', help='Общее количество запросов')
    parser.add_argument('-ct', '--count_type', action='store_true', help='Общее количество запросов по типу')
    parser.add_argument('-mc', '--most_common', action='store_true', help='Топ 10 самых частых запросов')

    args = vars(parser.parse_args(argv))

    if args['count']:
        print(f'Общее количество запросов - {count_lines()}')
    if args['count_type']:
        print(f'Общее количество запросов по типу - {Counter(count_by_methods())}')
    if args['most_common']:
        print(f'{Counter(top10()).most_common(10)}')

    print(args)
    return 0


if __name__ == '__main__':
    exit(main())
