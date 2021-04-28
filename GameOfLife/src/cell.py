#!/usr/bin/env python3


class Cell:
    """ Class represents a cell in the overall game board """

    def __init__(self) -> None:
        """All cells are dead to begin with"""
        self._status = "Dead"

    def set_dead(self) -> None:
        """Set cell status to dead"""
        self._status = "Dead"

    def set_alive(self) -> None:
        """Set cell status to alive"""
        self._status = "Alive"

    def is_alive(self) -> bool:
        """Check if cell is alive or dead"""
        if self._status == "Alive":
            return True
        return False

    def get_status(self) -> str:
        """Return a character for dead and alive"""
        if self._status is "Alive":
            return 'O'
        return "."
