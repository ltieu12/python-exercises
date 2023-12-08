#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 7, 2023
Purpose: Kentucky Friar
"""

import argparse
import os.path
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, 'r').read().rstrip()

    return args


# --------------------------------------------------
def fry(word):
    """Drop the `g` from `-ing` words, change `you` to `y'all`"""

    match = re.search('(.+)ing$', word)
    if match:
        first = match.group(1)
        if re.search('[aeiouy]', first.lower()):
            return match.group(1) + "in'"
    else:
        match = re.match('([yY])ou$', word)
        if match:
            return match.group(1) + "\'all"

    return word


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        words = [fry(word) for word in re.split(r'(\W+)', line.rstrip())]
        print(''.join(words))


# --------------------------------------------------
def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"


# --------------------------------------------------
if __name__ == '__main__':
    main()