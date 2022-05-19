from rubiks_cube import rubiks_cube
import pytest
import numpy 

################################################################################
# This file is to test the functionality of the rotate_r() method only. It does
# use other methods from rubiks_cube, but it is primarily focused on testing the
# cube's R rotations. Tests for other methods can be found in their respective
# test files.
################################################################################

BLUE = 0
RED = 1
GREEN = 2
ORANGE = 3
WHITE = 4
YELLOW = 5
ROWSIZE = 3
MAXSIZE = 6

# Testing basic R rotation on the 0th layer
def test_basic_rotation_r():
    test_cube = rubiks_cube()
    test_cube.rotate_r(0, 1)
    output_faces = [0 for i in range(MAXSIZE)]
    output_faces[0] = [[BLUE, BLUE, WHITE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[YELLOW, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, GREEN] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, BLUE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(0, 1)
    output_faces[0] = [[BLUE, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[BLUE, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, YELLOW] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, WHITE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(0, 1)
    output_faces[0] = [[BLUE, BLUE, YELLOW] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[WHITE, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, BLUE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, GREEN] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    # The cube should now be solved again
    test_cube.rotate_r(0, 1)
    assert test_cube.is_solved()

# Tests single R rotations on middle and left layer
def test_basic_rotation_r_other_layers():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]

    # Testing middle layer first (layer 1)
    test_cube.rotate_r(1, 1)
    output_faces[0] = [[BLUE, WHITE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, YELLOW, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, GREEN, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, BLUE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(1, 1)
    output_faces[0] = [[BLUE, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(1, 1)
    output_faces[0] = [[BLUE, YELLOW, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, WHITE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, BLUE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, GREEN, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(1, 1)
    assert test_cube.is_solved()

    # Now to test the leftmost layer (layer 2)
    test_cube.rotate_r(2, 1)
    output_faces[0] = [[WHITE, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, YELLOW] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[GREEN, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[BLUE, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(2, 1)
    output_faces[0] = [[GREEN, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[WHITE, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(2, 1)
    output_faces[0] = [[YELLOW, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, WHITE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[BLUE, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[GREEN, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(2, 1)
    assert test_cube.is_solved()

# Tests multiple rotations on the 0th layer
def test_multi_turns_layer_zero():
    test_cube = rubiks_cube()
    # Testing 2 R rotations
    test_cube.rotate_r(0, 2)
    output_faces = [0 for i in range(MAXSIZE)] 
    output_faces[0] = [[BLUE, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[BLUE, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, YELLOW] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, WHITE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(0, 3)
    output_faces[0] = [[BLUE, BLUE, WHITE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[YELLOW, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, GREEN] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, BLUE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(0, 4)
    assert test_cube.compare_to(output_faces)

    # Testing 5 rotations, should be equivalent to 1 rotation
    test_cube.rotate_r(0, 5)
    output_faces[0] = [[BLUE, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[BLUE, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, YELLOW] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, WHITE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

def test_multi_turns_other_layers():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]
    # Testing 2 R rotations on layer 1 first
    test_cube.rotate_r(1, 2)
    output_faces[0] = [[BLUE, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(1, 3)
    output_faces[0] = [[BLUE, WHITE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, YELLOW, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, GREEN, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, BLUE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(1, 4)
    assert test_cube.compare_to(output_faces)

    # Testing 5 rotations, should be equivalent to 1 rotation
    test_cube.rotate_r(1, 5)
    output_faces[0] = [[BLUE, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    # Now testing multi rotations on layer 2
    test_cube.rotate_r(2, 2)
    output_faces[0] = [[GREEN, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[WHITE, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(2, 3)
    output_faces[0] = [[WHITE, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, YELLOW] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[GREEN, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[BLUE, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(2, 4)
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(2, 5)
    output_faces[0] = [[GREEN, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[WHITE, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

def test_side_layer_rotation():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]
    # Initial moves intended to scramble the right and left faces
    test_cube.rotate_u(0, 1)
    test_cube.rotate_f(0, 1)
    test_cube.rotate_u(0, 2)
    output_faces[0] = [[ORANGE, ORANGE, ORANGE], [BLUE, BLUE, RED], [BLUE, BLUE, RED]]
    output_faces[1] = [[BLUE, BLUE, WHITE], [YELLOW, RED, RED], [YELLOW, RED, RED]]
    output_faces[2] = [[BLUE, BLUE, RED], [GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[YELLOW, GREEN, GREEN], [ORANGE, ORANGE, WHITE], [ORANGE, ORANGE, WHITE]]
    output_faces[4] = [[RED, RED, GREEN], [WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[BLUE, ORANGE, ORANGE], [YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    # Now use R rotations on both layers to check if side faces are rotating
    test_cube.rotate_r(0, 1)
    output_faces[0] = [[ORANGE, ORANGE, GREEN], [BLUE, BLUE, WHITE], [BLUE, BLUE, WHITE]]
    output_faces[1] = [[YELLOW, YELLOW, BLUE], [RED, RED, BLUE], [RED, RED, WHITE]]
    output_faces[2] = [[YELLOW, BLUE, RED], [YELLOW, GREEN, GREEN], [ORANGE, GREEN, GREEN]]
    # output_faces[3] should be unchanged by the rotation
    output_faces[4] = [[RED, RED, GREEN], [WHITE, WHITE, GREEN], [WHITE, WHITE, BLUE]]
    output_faces[5] = [[BLUE, ORANGE, ORANGE], [YELLOW, YELLOW, RED], [YELLOW, YELLOW, RED]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(0, 2)
    output_faces[0] = [[ORANGE, ORANGE, ORANGE], [BLUE, BLUE, YELLOW], [BLUE, BLUE, YELLOW]]
    output_faces[1] = [[WHITE, RED, RED], [BLUE, RED, RED], [BLUE, YELLOW, YELLOW]]
    output_faces[2] = [[WHITE, BLUE, RED], [WHITE, GREEN, GREEN], [GREEN, GREEN, GREEN]]
    # output_faces[3] should be unchanged by the rotation
    output_faces[4] = [[RED, RED, ORANGE], [WHITE, WHITE, RED], [WHITE, WHITE, RED]]
    output_faces[5] = [[BLUE, ORANGE, GREEN], [YELLOW, YELLOW, GREEN], [YELLOW, YELLOW, BLUE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(0, 3)
    output_faces[0] = [[ORANGE, ORANGE, GREEN], [BLUE, BLUE, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[RED, RED, YELLOW], [RED, RED, YELLOW], [WHITE, BLUE, BLUE]]
    output_faces[2] = [[RED, BLUE, RED], [RED, GREEN, GREEN], [ORANGE, GREEN, GREEN]]
    # output_faces[3] should be unchanged by the rotation
    output_faces[4] = [[RED, RED, ORANGE], [WHITE, WHITE, YELLOW], [WHITE, WHITE, YELLOW]]
    output_faces[5] = [[BLUE, ORANGE, GREEN], [YELLOW, YELLOW, WHITE], [YELLOW, YELLOW, WHITE]]
    assert test_cube.compare_to(output_faces)

    # Now to test rotation on the left face
    test_cube.rotate_r(2, 1)
    output_faces[0] = [[RED, ORANGE, GREEN], [WHITE, BLUE, GREEN], [WHITE, BLUE, BLUE]]
    # output_faces[1] should be unchanged by the rotation
    output_faces[2] = [[RED, BLUE, YELLOW], [RED, GREEN, YELLOW], [ORANGE, GREEN, BLUE]]
    output_faces[3] = [[GREEN, WHITE, WHITE], [GREEN, ORANGE, ORANGE], [YELLOW, ORANGE, ORANGE]]
    output_faces[4] = [[GREEN, RED, ORANGE], [GREEN, WHITE, YELLOW], [RED, WHITE, YELLOW]]
    output_faces[5] = [[ORANGE, ORANGE, GREEN], [BLUE, YELLOW, WHITE], [BLUE, YELLOW, WHITE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(2, 2)
    output_faces[0] = [[BLUE, ORANGE, GREEN], [YELLOW, BLUE, GREEN], [YELLOW, BLUE, BLUE]]
    # output_faces[1] should be unchanged by the rotation
    output_faces[2] = [[RED, BLUE, WHITE], [RED, GREEN, WHITE], [ORANGE, GREEN, RED]]
    output_faces[3] = [[ORANGE, ORANGE, YELLOW], [ORANGE, ORANGE, GREEN], [WHITE, WHITE, GREEN]]
    output_faces[4] = [[ORANGE, RED, ORANGE], [BLUE, WHITE, YELLOW], [BLUE, WHITE, YELLOW]]
    output_faces[5] = [[GREEN, ORANGE, GREEN], [GREEN, YELLOW, WHITE], [RED, YELLOW, WHITE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_r(2, 3)
    output_faces[0] = [[GREEN, ORANGE, GREEN], [GREEN, BLUE, GREEN], [RED, BLUE, BLUE]]
    # output_faces[1] should be unchanged by the rotation
    output_faces[2] = [[RED, BLUE, BLUE], [RED, GREEN, BLUE], [ORANGE, GREEN, ORANGE]]
    output_faces[3] = [[WHITE, ORANGE, ORANGE], [WHITE, ORANGE, ORANGE], [GREEN, GREEN, YELLOW]]
    output_faces[4] = [[BLUE, RED, ORANGE], [YELLOW, WHITE, YELLOW], [YELLOW, WHITE, YELLOW]]
    output_faces[5] = [[RED, ORANGE, GREEN], [WHITE, YELLOW, WHITE], [WHITE, YELLOW, WHITE]]
    assert test_cube.compare_to(output_faces)
