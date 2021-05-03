import argparse
from typing import Optional
from typing import Sequence

PATH_TO_ACCESS_LOG = 'access.log'


def count_lines(filename=PATH_TO_ACCESS_LOG):
    with open(filename) as f:
        return sum(1 for line in f if line.strip())


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--count', action='store_true', help='Общее количество запросов')

    args = vars(parser.parse_args(argv))

    if args['count']:
        print(f'Общее количество запросов - {count_lines()}')

    print(args)
    return 0


if __name__ == '__main__':
    exit(main())
