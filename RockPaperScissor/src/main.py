#!/usr/bin/env python3
from player import Player
from game import Game


def main():
    """ Main method were we start the game from """
    print("--- ROCK PAPER SCISSOR ---\n")

    # Get some needed input before we start the game
    name = input("What is your name?\n> ")
    player = Player(name)
    print(f"\nHello, {name}! Welcome to Rock, Paper, Scissor\n")
    game = Game()

    # Start game
    game.play(player)


if __name__ == "__main__":
    main()
