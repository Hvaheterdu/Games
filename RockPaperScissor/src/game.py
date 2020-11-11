#!/usr/bin/env python3
from player import Player
import random
import os
import time


ROCK = "Rock"
PAPER = "Paper"
SCISSOR = "Scissor"
CHOICES = [ROCK, PAPER, SCISSOR]


class Game:
    """ Game class """

    def play(self, player):
        """ Method we run the game from """
        self.compute(player)

    def compute(self, player):
        """Compute who wins when. Computer choices are made
        by random"""
        computer_score = 0
        player_score = 0
        computer_choice = random.choice(CHOICES)

        while True:
            player_choice = input(
                "Rock, Paper og Scissor? Press 'q' to exit the game\n> ")

            # Quit program
            if player_choice == 'q':
                print("Game terminated")
                break

            # Draw
            if computer_choice == player_choice.capitalize():
                print(f"\nComputer chooses {computer_choice}\n")
                print("It's a draw. Nobody gets any points\n")
            elif computer_choice == player_choice.capitalize():
                print(f"\nComputer chooses {computer_choice}\n")
                print("It's a draw. Nobody gets any points\n")
            elif computer_choice == player_choice.capitalize():
                print(f"\nComputer chooses {computer_choice}\n")
                print("It's a draw. Nobody gets any points\n")

            # Computer wins
            if computer_choice == ROCK and player_choice.capitalize() == SCISSOR:
                computer_score += 1
                print(f"\nComputer chooses {computer_choice}\n")
                print("Computer wins. Computer gets one point\n")
            elif computer_choice == PAPER and player_choice.capitalize() == ROCK:
                computer_score += 1
                print(f"\nComputer chooses {computer_choice}\n")
                print("Computer wins. Computer gets one point\n")
            elif computer_choice == SCISSOR and player_choice.capitalize() == PAPER:
                computer_score += 1
                print(f"\nComputer chooses {computer_choice}\n")
                print("Computer wins. Computer gets one point\n")

            # Player wins
            if player_choice.capitalize() == ROCK and computer_choice == SCISSOR:
                player_score += 1
                print(f"\nComputer chooses {computer_choice}\n")
                print(
                    f"{player.get_name()} wins. {player.get_name()} gets one point\n")
            elif player_choice.capitalize() == PAPER and computer_choice == ROCK:
                player_score += 1
                print(f"\nComputer chooses {computer_choice}\n")
                print(
                    f"{player.get_name()} wins. {player.get_name()} gets one point\n")
            elif player_choice.capitalize() == SCISSOR and computer_choice == PAPER:
                player_score += 1
                print(f"\nComputer chooses {computer_choice}\n")
                print(
                    f"{player.get_name()} wins. {player.get_name()} gets one point\n")

            print("Total scores are: ")
            print(f"Computer: {computer_score}")
            print(f"Player:   {player_score}\n")
