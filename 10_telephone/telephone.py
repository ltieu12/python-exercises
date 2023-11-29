#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Nov 29, 2023
Purpose: Telephone
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()
    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text, 'r').read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    # number of letter will be replaced
    num_mutation = round(len(args.text) * args.mutations)
    # list of characters that will replace (choose randomly)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    # list of indexes that will be replaced
    replace_indexes = random.sample(range(len(args.text)), num_mutation)
    new_text = args.text
    print(f'You said: "{args.text}"')

    for i in replace_indexes:
        # slice string before and after replacing index
        text_1 = new_text[:i]
        text_3 = new_text[(i + 1):]
        # randomly chosen char from alpha to replace char at chosen index
        text_2 = random.choice(alpha.replace(new_text[i], ''))
        new_text = text_1 + text_2 + text_3

    print(f'I heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
