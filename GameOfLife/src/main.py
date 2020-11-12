#!/usr/bin/env python3
from gameboard import GameBoard
import argparse


def main():
    """ Creates board and runs the game """
    parser = argparse.ArgumentParser(
        description='Conways Game of life that runs for as many generations as you like')

    parser.add_argument('x', type=int, help='Size of x-axis')
    parser.add_argument('y', type=int, help='Size of y-axis')
    args = parser.parse_args()

    # Create board
    board = GameBoard(args.x, args.y)

    # Program loop
    finished = "a"
    while finished != 'q':
        board.draw_board()
        finished = input(
            "Press enter continue and 'q' to quit\n> ")
        if finished.lower() == "q":
            print("Program terminated")


if __name__ == "__main__":
    main()
