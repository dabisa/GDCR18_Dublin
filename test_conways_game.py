'''
Test
'''

from conways_game import *


def test_if_cell_is_alive():
    state = CellState.Alive
    assert state == CellState.Alive

def test_if_cell_is_dead():
    state = CellState.Dead
    assert state == CellState.Dead

def test_empty_environment():
    environment = Environment()
    assert environment.number_of_alive_cells() == 0

def test_environment_of_two_alive_cell():
    environment = Environment(2)
    assert environment.number_of_alive_cells() == 2

def test_environment_of_three_alive_cell():
    environment = Environment(3)
    assert environment.number_of_alive_cells() == 3

def test_environment_of_four_alive_cell():
    environment = Environment(4)
    assert environment.number_of_alive_cells() == 4

def test_center_position():
    coordinate = Coordinate()
    assert coordinate.x() == 0
    assert coordinate.y() == 0

def test_getting_environment_from_grid():
    # setup
    grid = Grid()
    coordinate = Coordinate()

    # action
    environment = grid.get_environment(coordinate)

    # test
    assert environment.number_of_alive_cells() == 0

