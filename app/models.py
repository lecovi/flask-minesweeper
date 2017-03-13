"""
    minesweeper.models
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description
    
    :copyright: (c) 2017 by LeCoVi.
    :author: Leandro E. Colombo Viña <colomboleandro at bitson.com.ar>.
    :license: AGPL, see LICENSE for more details.
"""
# Standard lib imports
from random import choice
# Third-party imports
# LeCoVi imports


class Tile:
    """This class will represent each Tile."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_mine = False
        self.is_revealed = False
        self.is_marked = False
        self.mines_around = 0

    def get_neighbours(self, board):
        neighbours_list = list()
        if self.y == 0:
            neighbours_list.append(board.tiles[self.x][self.y + 1])
            if self.x == 0:
                neighbours_list.append(board.tiles[self.x + 1][self.y])
                neighbours_list.append(board.tiles[self.x + 1][self.y + 1])
            elif self.x == board.width - 1:
                neighbours_list.append(board.tiles[self.x - 1][self.y])
                neighbours_list.append(board.tiles[self.x - 1][self.y + 1])
            else:
                neighbours_list.append(board.tiles[self.x - 1][self.y])
                neighbours_list.append(board.tiles[self.x + 1][self.y])
                neighbours_list.append(board.tiles[self.x - 1][self.y + 1])
                neighbours_list.append(board.tiles[self.x + 1][self.y + 1])
        elif self.y == board.height - 1:
            neighbours_list.append(board.tiles[self.x][self.y - 1])
            if self.x == 0:
                neighbours_list.append(board.tiles[self.x + 1][self.y - 1])
                neighbours_list.append(board.tiles[self.x + 1][self.y])
            elif self.x == board.width - 1:
                neighbours_list.append(board.tiles[self.x - 1][self.y - 1])
                neighbours_list.append(board.tiles[self.x - 1][self.y])
            else:
                neighbours_list.append(board.tiles[self.x - 1][self.y - 1])
                neighbours_list.append(board.tiles[self.x + 1][self.y - 1])
                neighbours_list.append(board.tiles[self.x - 1][self.y])
                neighbours_list.append(board.tiles[self.x + 1][self.y])
        else:
            neighbours_list.append(board.tiles[self.x][self.y - 1])
            neighbours_list.append(board.tiles[self.x][self.y + 1])
            if self.x == 0:
                neighbours_list.append(board.tiles[self.x + 1][self.y - 1])
                neighbours_list.append(board.tiles[self.x + 1][self.y])
                neighbours_list.append(board.tiles[self.x - 1][self.y + 1])
            elif self.x == board.width - 1:
                neighbours_list.append(board.tiles[self.x - 1][self.y - 1])
                neighbours_list.append(board.tiles[self.x - 1][self.y])
                neighbours_list.append(board.tiles[self.x - 1][self.y + 1])
            else:
                neighbours_list.append(board.tiles[self.x - 1][self.y - 1])
                neighbours_list.append(board.tiles[self.x + 1][self.y - 1])
                neighbours_list.append(board.tiles[self.x - 1][self.y])
                neighbours_list.append(board.tiles[self.x + 1][self.y])
                neighbours_list.append(board.tiles[self.x - 1][self.y + 1])
                neighbours_list.append(board.tiles[self.x + 1][self.y + 1])
        return neighbours_list


class Board:
    """This class will represent the whole Board, a set of class:`Tile`"""

    def __init__(self, width=15, height=15, mines=30):
        self.width = width
        self.height = height
        self.mines = mines
        self.tiles = list()
        self._new_board()

    def _new_board(self):
        for x in range(self.height):
            self.tiles.append(list())
            for y in range(self.width):
                new_tile = Tile(x=x, y=y)
                self.tiles[x].append(new_tile)

    def set_mines(self):
        mines_left = self.mines
        while mines_left > 0:
            random_row = choice(range(self.width))
            random_col = choice(range(self.height))
            if not self.tiles[random_row][random_col].has_mine:
                self.tiles[random_row][random_col].has_mine = True
            mines_left -= 1

    def calculate_mines(self):
        for row in self.tiles:
            for tile in row:
                for neighbour in tile.get_neighbours(board=self):
                    if neighbour.has_mine:
                        tile.mines_around += 1
