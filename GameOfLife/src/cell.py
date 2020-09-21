#!/user/bin/env python3
class Cell:
    """ Class represents a cell in the overall game board """

    def __init__(self):
        """ All cells are dead to begin with """
        self._status = "Dead"

    def set_dead(self):
        """ Set cell status to dead """
        self._status = "Dead"

    def set_alive(self):
        """ Set cell status to alive """
        self._status = "Alive"

    def is_alive(self):
        """ Check if cell is alive or dead """
        if self._status == "Alive":
            return True
        elif self._status == "Dead":
            return False

    def get_status(self):
        """ Return a character for dead and alive """
        if self._status is "Alive":
            return 'O'
        elif self._status is "Dead":
            return "."
