#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : todayNov 20, 2023
Purpose: Word Count Program
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_lines = 0
    total_words = 0
    total_bytes = 0
    for file_handle in args.FILE:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in file_handle:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)

        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes

        result = '{:8}{:8}{:8} {}'.format(num_lines, num_words, num_bytes, file_handle.name)
        print(result)

    if len(args.FILE) > 1:
        print('{:8}{:8}{:8} total'.format(total_lines, total_words, total_bytes))


# --------------------------------------------------
if __name__ == '__main__':
    main()