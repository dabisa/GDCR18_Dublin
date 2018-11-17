'''
Code
'''

import enum

class CellState(enum.Enum):
    Alive = 0
    Dead = 1


class Environment(object):
    def __init__(self, count_of_alive_cells=0):
        self._count_of_alive_cells = count_of_alive_cells

    def number_of_alive_cells(self):
        return self._count_of_alive_cells

class Coordinate(object):
    def __init__(self):
        self._x = 0
        self._y = 0

    def x(self):
        return self._x

    def y(self):
        return self._y



'''
class Grid(object):
    def __init__(self, alive_cells):
'''
