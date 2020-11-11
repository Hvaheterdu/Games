#!/usr/bin/env python3

class Player:
    """ Player class """

    def __init__(self, name) -> None:
        """ Constructor, gets players name """
        self.name = name

    def get_name(self):
        """ Return players name """
        return self.name
