#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 8, 2023
Purpose: Scrambler
"""

import argparse
import os.path
import re
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input file or text')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, 'r').read().rstrip()

    return args


# --------------------------------------------------
def scramble(word):
    if len(word) < 4:
        return word
    else:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in args.text.splitlines():
        print(''.join(map(scramble, splitter.split(line))))


# --------------------------------------------------
def test_scramble():
    """Test scramble"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()