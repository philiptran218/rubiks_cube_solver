from rubiks_cube import rubiks_cube
import pytest
import numpy 

BLUE = 0
RED = 1
GREEN = 2
ORANGE = 3
WHITE = 4
YELLOW = 5
ROWSIZE = 3
MAXSIZE = 6

# test_cube should be a solved cube in its initial state
def test_correct_initial_state():
    test_cube = rubiks_cube()
    assert test_cube.is_solved()

def test_is_solved():
    test_cube = rubiks_cube()
    # Try scrambling the cube to check if it's now unsolved
    test_cube.rotate_r(0, 1)
    test_cube.rotate_f(0, 1)
    assert not test_cube.is_solved()

    # Now the cube will be solved again
    test_cube.rotate_b(2, 1)
    test_cube.rotate_l(2, 1)
    assert test_cube.is_solved()

# Testing if the scramble function work. Cube should not be in a solved state.
def test_scramble():
    test_cube = rubiks_cube()
    test_cube.scramble(10)
    assert not test_cube.is_solved()

