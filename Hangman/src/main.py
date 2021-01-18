#!/usr/bin/env python3
from game import Hangman


def main() -> None:
    """ Main method were we start the game """

    # Start game
    game = Hangman()
    game.play()


if __name__ == "__main__":
    main()
