#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 12, 2023
Purpose: Gematria
"""

import argparse
import os.path
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, 'r').read().rstrip()

    return args


# --------------------------------------------------
def word2num(word):
    new_word = re.sub('[^A-Za-z0-9]', '', word)
    vals = [ord(char) for char in new_word]
    return str(sum(vals))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        encode = []
        for word in line.split():
            encode.append(word2num(word))
        print(' '.join(encode))


# --------------------------------------------------
if __name__ == '__main__':
    main()