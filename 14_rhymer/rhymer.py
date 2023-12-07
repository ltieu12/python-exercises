#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 6, 2023
Purpose: Rhymer (Regular Expression)
"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def stemmer(text):
    """Return leading consonants (if any), and 'stem' of word"""
    consonants = ''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])
    pattern = '[' + consonants + ']'
    match = re.match(f'([{consonants}]+)?([aeiou])(.*)', text, re.IGNORECASE)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
        return (text, '')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    consonants = [c for c in string.ascii_lowercase if c not in 'aeiou']
    consonants.extend(['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl',
                       'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'thw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph',
                       'spl', 'spr', 'squ', 'str', 'thr'])
    consonants.sort()
    split_word = stemmer(args.word)
    if split_word[1] == '':
        print(f'Cannot rhyme "{args.word}"')
    else:
        for c in consonants:
            if c != split_word[0].lower():
                print(c + split_word[1].lower())


# --------------------------------------------------
if __name__ == '__main__':
    main()
