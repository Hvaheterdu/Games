#!/usr/bin/env python3
import pygame


class Game:

    def __init__(self) -> None:
        """ Constructor """
        pygame.init()

    def play(self) -> None:
        """ Start the game """
        self._draw()

    def _draw(self) -> None:
        """ Create elements and draw the game """
        pass
