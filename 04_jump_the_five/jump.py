#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Nov 17, 2023
Purpose: Jump the five Encoding/Decoding
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.str
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    for char in input:
        if char in jumper.keys():
            val = jumper.get(char)
            char = val
        print(char, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
