'''
Test
'''

from conways_game import *


def test_is_alive():
    state = Alive()
    assert state.is_alive() == True

def test_is_dead():
    state = Dead()
    assert state.is_alive() == False
