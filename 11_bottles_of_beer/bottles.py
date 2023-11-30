#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Nov 30, 2023
Purpose: Bottles of beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()
    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def verse(bottles):
    """Sing a verse"""
    if bottles > 1:
        text = "bottles"
        if bottles - 1 > 1:
            last_line = f'{bottles - 1} bottles of beer on the wall!\n'
        else:
            last_line = f'{bottles - 1} bottle of beer on the wall!\n'
    else:
        text = "bottle"
        last_line = "No more bottles of beer on the wall!"

    print(f'{bottles} {text} of beer on the wall,\n'
          f'{bottles} {text} of beer,\n'
          f'Take one down, pass it around,\n'
          f'{last_line}')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for num in list(reversed(range(1, args.num + 1))):
        verse(num)


# --------------------------------------------------
if __name__ == '__main__':
    main()
