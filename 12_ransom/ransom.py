#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 1, 2023
Purpose: Ransom Note
"""

import argparse
import os.path
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, 'r').read().strip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    new_text = ''
    for char in args.text:
        new_text += choose(char)
    print(new_text)


# --------------------------------------------------
def choose(char):
    """Randomly choose uppercase or lowercase letter to return"""
    if random.choice([0, 1]) == 0:
        return char.lower()
    else:
        return char.upper()


# --------------------------------------------------
if __name__ == '__main__':
    main()