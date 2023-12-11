#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 11, 2023
Purpose: Mad Libs
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs='*',
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.FILE.read().rstrip()
    matches = re.findall('(<([^<>]+)>)', text)
    if not matches:
        sys.exit(f'"{args.FILE.name}" has no placeholders.')

    replace_text = text
    if args.inputs is None:
        for placeholder, name in matches:
            article = 'an' if name[0] in 'aeiou' else 'a'
            value = input(f'Give me {article} {name}: ')
            replace_text = re.sub(f'(<{name}>)', value, replace_text, count=1)
    else:
        for placeholder, name in matches:
            value = args.inputs.pop(0)
            replace_text = re.sub(f'(<{name}>)', value, replace_text, count=1)

    print(replace_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()