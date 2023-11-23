#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Nov 20, 2023
Purpose: Apples and Bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        choices=['a', 'i', 'e', 'o', 'u'],
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    string = args.text
    replace_vowel = args.vowel

    lookup = {}
    for vowel in 'aieou':
        lookup[vowel] = replace_vowel

    for vowel in 'AIEOU':
        lookup[vowel] = replace_vowel.upper()

    if os.path.isfile(string):
        with open(string, 'r') as file:
            text = file.read()
        print(text.translate(str.maketrans(lookup)))
    else:
        print(string.translate(str.maketrans(lookup)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
