#!/usr/bin/env python3
"""
Author :  Lam Tieu
Date   :  Nov 8, 2023
Purpose:  Picnic trip
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Item(s) to bring',
                        nargs='+')
    parser.add_argument('-s', '--sorted',
                        help="Sort the items",
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.str
    sort_flag = args.sorted

    if sort_flag:
        items.sort()

    if len(items) == 1:
        print(f'You are bringing {items[0]}.')
    elif len(items) == 2:
        print(f'You are bringing {items[0]} and {items[1]}.')
    else:
        last_index = len(items) - 1
        comma_list = ', '.join(items[0:last_index])
        print(f'You are bringing {comma_list}, and {items[-1]}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()