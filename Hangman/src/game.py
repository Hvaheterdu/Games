#!/usr/bin/env python3
import pygame
import random
import os


# Colour and screen size
WIDTH = 1000
HEIGHT = 800
BUTTON_COLOUR = (153, 204, 255)
WHITE = (255, 255, 255)
TEXT_COLOUR = (0, 0, 0)

# Parent directory and directory with folder that contains words file
PARENT_FOLDER = os.path.dirname(os.path.dirname(__file__))
WORD_FOLDER = os.path.join(PARENT_FOLDER + '/words')


class Hangman:

    def __init__(self) -> None:
        """Constructor"""
        pygame.init()

    def play(self) -> None:
        """Start the game"""
        self._game()

    def _game(self) -> None:
        """Create elements and draw the game"""
        solution = self._solution().lower()
        max_tries = 10
        tries = 0

        # Create screen, fill background and add window title
        self.screen = self._create_screen()
        self.screen.fill(WHITE)
        pygame.display.set_caption('Hangman')

        # Loop for when user is guessing the word
        while tries < max_tries:
            pass

    def _solution(self) -> str:
        """Return a solution word from file"""
        file_handler = open(WORD_FOLDER + '/words.txt').read().split()
        solution = random.choice(file_handler)
        return solution

    def _create_screen(self) -> pygame.Surface:
        """Create screen to draw on"""
        return pygame.display.set_mode((WIDTH, HEIGHT))
