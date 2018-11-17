'''
Code
'''

class CellState(object):
    def is_alive(self):
        return self._is_alive


class Alive(CellState):
    def __init__(self):
        self._is_alive = True


class Dead(CellState):
    def __init__(self):
        self._is_alive = False
