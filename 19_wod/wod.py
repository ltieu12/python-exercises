#!/usr/bin/env python3
"""
Author : Lam Tieu
Date   : Dec 13, 2023
Purpose: Workout of the Day
"""

import argparse
import csv
import random
import re
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()
    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""
    reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        match = re.match(r'(\d+)-(\d+)', reps)
        low = int(match.group(1))
        high = int(match.group(2))
        exercises.append((name, low, high))

    return exercises


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    to_do = random.sample(read_csv(args.file), k=args.num)
    wod = []
    for ex in to_do:
        reps = random.randint(ex[1], ex[-1])
        if args.easy:
            reps = int(reps/2)
        wod.append((ex[0], reps))

    print(tabulate(wod, headers=('Exercise', 'Reps')))


# --------------------------------------------------
if __name__ == '__main__':
    main()