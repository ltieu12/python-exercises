#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 5, 2023
Purpose: Twelve days of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()
    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def verse(num):
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gifts_list = ['A partridge in a pear tree',
                  'Two turtle doves',
                  'Three French hens',
                  'Four calling birds',
                  'Five gold rings',
                  'Six geese a laying',
                  'Seven swans a swimming',
                  'Eight maids a milking',
                  'Nine ladies dancing',
                  'Ten lords a leaping',
                  'Eleven pipers piping',
                  'Twelve drummers drumming']
    gifts = ''
    for day in reversed(range(1, num + 1)):
        if day == 1:
            if num > 1:
                gifts += "And a partridge in a pear tree."
            else:
                gifts += gifts_list[0] + '.\n'
        else:
            gifts += gifts_list[day - 1] + ',\n'
    return (f'On the {ordinal[num - 1]} day of Christmas,\n'
            f'My true love gave to me,\n'
            f'{gifts}\n')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for day in range(1, args.num + 1):
        if day != 1 and day != args.num:
            args.outfile.write(verse(day) + '\n')
        else:
            args.outfile.write(verse(day))


# --------------------------------------------------
if __name__ == '__main__':
    main()