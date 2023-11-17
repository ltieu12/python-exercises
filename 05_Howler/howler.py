#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Nov 17, 2023
Purpose: Howler
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.text
    output = args.outfile

    if os.path.isfile(input):
        with open(input, 'r') as input_file:
            text = input_file.read().upper()
    else:
        text = input.upper()

    if output != '':
        with open(output, 'wt') as output_file:
            output_file.write(text)
    else:
        print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
