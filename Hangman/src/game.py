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
        """ Constructor """
        pygame.init()

    def play(self) -> None:
        """ Start the game """
        self._draw()

    def _draw(self) -> None:
        """ Create elements and draw the game """
        max_tries = 10
        tries = 0

    def _solution(self) -> str:
        """ Return a solution word from file """
        file_handler = open(WORD_FOLDER + '/words.txt').read().split()
        solution = random.choice(file_handler)
        return solution
