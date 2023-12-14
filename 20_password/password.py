#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 13, 2023
Purpose: Password
"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def clean(word):
    """Remove any non-letter character in a word"""

    new_word = re.sub(r'\W', '', word)
    return new_word


# --------------------------------------------------
def ransom(word):
    """Randomly choose letter to be upper or lowercase"""

    new_word = ''
    for char in word:
        if random.choice([0, 1]) == 0:
            new_word += char.lower()
        else:
            new_word += char.upper()

    return new_word


# --------------------------------------------------
def l33t(word):
    """Encode certain characters of a word to another character and add a random punctuation"""

    word = ransom(word)
    new_word = ''
    encode = {'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'}
    for char in word:
        new_word += encode[char] if encode.get(char) is not None else char

    return new_word + random.choice(string.punctuation)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    passwords = []
    for num in range(args.num):
        passwords.append(''.join(random.sample(words, args.num_words)))

    for password in passwords:
        if args.l33t:
            print(l33t(password))
        else:
            print(password)


# --------------------------------------------------
if __name__ == '__main__':
    main()