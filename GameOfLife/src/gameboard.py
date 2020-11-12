#!/usr/bin/env python3
from random import randint
from cell import Cell
import os


class GameBoard:
    """ Class that creates the game board """

    def __init__(self, row, column):
        """ Constructor """
        self._row = row
        self._column = column
        self._grid = [[Cell() for y in range(self._row)]
                      for x in range(self._column)]
        self.generation_num = 0
        self._generate()

    def draw_board(self):
        """ Draw game board """
        os.system('clear')
        for x in range(self._column):
            for y in range(self._row):
                print(self._grid[x][y].get_status(), end='')
            print()
        print(
            f"Generation: {self.generation_num} - Living cells: {self.find_all_alive()}")
        self.update()

    def update(self):
        """ Updates each cell according to the game rules """
        dead_become_alive = []
        alive_become_dead = []
        for x in range(self._column):
            for y in range(self._row):
                alive_cells = 0
                # Check neighbours after game rules
                for neighbours in self.find_neighbours(y, x):
                    if neighbours.is_alive():
                        alive_cells += 1
                if self._grid[x][y].is_alive():
                    if alive_cells < 2 or alive_cells > 3:
                        self._grid[x][y].set_dead()
                        alive_become_dead.append(self._grid[x][y])
                    elif alive_cells == 2 or alive_cells == 3:
                        self._grid[x][y].set_alive()
                else:
                    if alive_cells == 3:
                        self._grid[x][y].set_alive()
                        dead_become_alive.append(self._grid[x][y])
                    else:
                        self._grid[x][y].set_dead()

        for j in dead_become_alive:
            j.set_alive()
        for k in alive_become_dead:
            k.set_dead()

        self.generation_num += 1

    def find_all_alive(self):
        """ Return all alive cells """
        alive_cells = 0
        for x in range(self._column):
            for y in range(self._row):
                if self._grid[x][y].is_alive():
                    alive_cells += 1
        return alive_cells

    def _generate(self):
        """ Generate alive cells after game rules """
        for i in range(self._row):
            for j in range(self._column):
                rand = randint(0, 3)
                if rand == 3:
                    self._grid[j][i].set_alive()

    def find_neighbours(self, rows, columns):
        """ Return neighbours to every cell """
        neighbours_array = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbours_rows = rows + i
                neighbours_columns = columns + j
                if not (neighbours_rows == rows and neighbours_columns == columns):
                    if not (neighbours_rows < 0 or neighbours_columns < 0 or neighbours_rows > self._row - 1
                            or neighbours_columns > self._column - 1):
                        neighbours_array.append(
                            self._grid[neighbours_columns][neighbours_rows])
        return neighbours_array
