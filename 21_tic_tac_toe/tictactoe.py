#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='The state of the board',
                        metavar='board',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='player',
                        choices='XO',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='cell',
                        type=int,
                        choices=range(1, 10),
                        default=None)

    args = parser.parse_args()
    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both --player and --cell')
    if not re.search('^[.XO]{9}$', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')
    if args.player and args.cell and args.board[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def format_board(board_str):
    board = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    for i, char in enumerate(board_str, 1):
        if char == 'X':
            board = board.replace(str(i), 'X')
        elif char == 'O':
            board = board.replace(str(i), 'O')
    return board


# --------------------------------------------------
def find_winner(board):
    pass


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.board)
    print(format_board(args.board))


# --------------------------------------------------
if __name__ == '__main__':
    main()