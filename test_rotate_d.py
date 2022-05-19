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

# Testing basic D rotation on the 0th layer
def test_basic_rotation_d():
    test_cube = rubiks_cube()
    test_cube.rotate_d(0, 1)
    output_faces = [0 for i in range(MAXSIZE)]
    output_faces[0] = [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [ORANGE, ORANGE, ORANGE]]
    output_faces[1] = [[RED, RED, RED], [RED, RED, RED], [BLUE, BLUE, BLUE]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [RED, RED, RED]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [GREEN, GREEN, GREEN]]
    output_faces[4] = [[WHITE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[5] = [[YELLOW for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(0, 1)
    output_faces[0] = [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[1] = [[RED, RED, RED], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(0, 1)
    output_faces[0] = [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [RED, RED, RED]]
    output_faces[1] = [[RED, RED, RED], [RED, RED, RED], [GREEN, GREEN, GREEN]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [ORANGE, ORANGE, ORANGE]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [BLUE, BLUE, BLUE]]
    assert test_cube.compare_to(output_faces)

    # The cube should now be solved again
    test_cube.rotate_d(0, 1)
    assert test_cube.is_solved()

# Tests single D rotations on middle and right layer
def test_basic_rotation_d_other_layers():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]

    # Testing middle layer first (layer 1)
    test_cube.rotate_d(1, 1)
    output_faces[0] = [[BLUE, BLUE, BLUE], [ORANGE, ORANGE, ORANGE], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[RED, RED, RED], [BLUE, BLUE, BLUE], [RED, RED, RED]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [RED, RED, RED], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [GREEN, GREEN, GREEN], [ORANGE, ORANGE, ORANGE]]
    output_faces[4] = [[WHITE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[5] = [[YELLOW for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(1, 1)
    output_faces[0] = [[BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[RED, RED, RED], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(1, 1)
    output_faces[0] = [[BLUE, BLUE, BLUE], [RED, RED, RED], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[RED, RED, RED], [GREEN, GREEN, GREEN], [RED, RED, RED]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [ORANGE, ORANGE, ORANGE], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [BLUE, BLUE, BLUE], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(1, 1)
    assert test_cube.is_solved()

    # Now to test the top layer (layer 2)
    test_cube.rotate_d(2, 1)
    output_faces[0] = [[ORANGE, ORANGE, ORANGE], [BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[BLUE, BLUE, BLUE], [RED, RED, RED], [RED, RED, RED]]
    output_faces[2] = [[RED, RED, RED], [GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[GREEN, GREEN, GREEN], [ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(2, 1)
    output_faces[0] = [[GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[ORANGE, ORANGE, ORANGE], [RED, RED, RED], [RED, RED, RED]]
    output_faces[2] = [[BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[RED, RED, RED], [ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(2, 1)
    output_faces[0] = [[RED, RED, RED], [BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[GREEN, GREEN, GREEN], [RED, RED, RED], [RED, RED, RED]]
    output_faces[2] = [[ORANGE, ORANGE, ORANGE], [GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[BLUE, BLUE, BLUE], [ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(2, 1)
    assert test_cube.is_solved()

# Tests multiple rotations on the 0th layer
def test_multi_turns_layer_zero():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)] 
    # Testing 2 D rotations
    test_cube.rotate_d(0, 2)
    output_faces[0] = [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[1] = [[RED, RED, RED], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    output_faces[4] = [[WHITE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[5] = [[YELLOW for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(0, 3)
    output_faces[0] = [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [ORANGE, ORANGE, ORANGE]]
    output_faces[1] = [[RED, RED, RED], [RED, RED, RED], [BLUE, BLUE, BLUE]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [RED, RED, RED]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [GREEN, GREEN, GREEN]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(0, 4)
    assert test_cube.compare_to(output_faces)

    # Testing 5 rotations, should be equivalent to 1 rotation
    test_cube.rotate_d(0, 5)
    output_faces[0] = [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[1] = [[RED, RED, RED], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    assert test_cube.compare_to(output_faces)
    
def test_multi_turns_other_layers():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]
    # Testing 2 D rotations on layer 1 first
    test_cube.rotate_d(1, 2)
    output_faces[0] = [[BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[RED, RED, RED], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    output_faces[4] = [[WHITE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[5] = [[YELLOW for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(1, 3)
    output_faces[0] = [[BLUE, BLUE, BLUE], [ORANGE, ORANGE, ORANGE], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[RED, RED, RED], [BLUE, BLUE, BLUE], [RED, RED, RED]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [RED, RED, RED], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [GREEN, GREEN, GREEN], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(1, 4)
    assert test_cube.compare_to(output_faces)

    # Testing 5 rotations, should be equivalent to 1 rotation
    test_cube.rotate_d(1, 5)
    output_faces[0] = [[BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[RED, RED, RED], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    output_faces[2] = [[GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[ORANGE, ORANGE, ORANGE], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    # Now testing multi rotations on layer 2
    test_cube.rotate_d(2, 2)
    output_faces[0] = [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    output_faces[2] = [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[RED, RED, RED], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(2, 3)
    output_faces[0] = [[ORANGE, ORANGE, ORANGE], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[BLUE, BLUE, BLUE], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    output_faces[2] = [[RED, RED, RED], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[GREEN, GREEN, GREEN], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(2, 4)
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(2, 5)
    output_faces[0] = [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    output_faces[1] = [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [RED, RED, RED]]
    output_faces[2] = [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [GREEN, GREEN, GREEN]]
    output_faces[3] = [[RED, RED, RED], [RED, RED, RED], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

def test_side_layer_rotation():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]
    # Initial moves intended to scramble the top and bottom faces
    test_cube.rotate_l(0, 1)
    test_cube.rotate_f(0, 1)
    test_cube.rotate_r(0, 1)
    output_faces[0] = [[YELLOW, YELLOW, RED], [BLUE, BLUE, WHITE], [BLUE, BLUE, WHITE]]
    output_faces[1] = [[YELLOW, YELLOW, GREEN], [RED, RED, RED], [RED, RED, RED]]
    output_faces[2] = [[ORANGE, GREEN, WHITE], [YELLOW, GREEN, WHITE], [YELLOW, GREEN, WHITE]]
    output_faces[3] = [[ORANGE, ORANGE, BLUE], [ORANGE, ORANGE, WHITE], [ORANGE, ORANGE, WHITE]]
    output_faces[4] = [[RED, RED, GREEN], [BLUE, WHITE, GREEN], [BLUE, WHITE, GREEN]]
    output_faces[5] = [[GREEN, YELLOW, YELLOW], [GREEN, YELLOW, BLUE], [ORANGE, ORANGE, BLUE]]
    assert test_cube.compare_to(output_faces)

    # Now use D rotations on both layers to check if top/bottom faces are rotating
    test_cube.rotate_d(0, 1)
    output_faces[0] = [[YELLOW, YELLOW, RED], [BLUE, BLUE, WHITE], [ORANGE, ORANGE, WHITE]]
    output_faces[1] = [[YELLOW, YELLOW, GREEN], [RED, RED, RED], [BLUE, BLUE, WHITE]]
    output_faces[2] = [[ORANGE, GREEN, WHITE], [YELLOW, GREEN, WHITE], [RED, RED, RED]]
    output_faces[3] = [[ORANGE, ORANGE, BLUE], [ORANGE, ORANGE, WHITE], [YELLOW, GREEN, WHITE]]
    output_faces[4] = [[BLUE, BLUE, RED], [WHITE, WHITE, RED], [GREEN, GREEN, GREEN]]
    # output_faces[5] should be unchanged by the rotation
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(0, 2)
    output_faces[0] = [[YELLOW, YELLOW, RED], [BLUE, BLUE, WHITE], [RED, RED, RED]]
    output_faces[1] = [[YELLOW, YELLOW, GREEN], [RED, RED, RED], [YELLOW, GREEN, WHITE]]
    output_faces[2] = [[ORANGE, GREEN, WHITE], [YELLOW, GREEN, WHITE], [ORANGE, ORANGE, WHITE]]
    output_faces[3] = [[ORANGE, ORANGE, BLUE], [ORANGE, ORANGE, WHITE], [BLUE, BLUE, WHITE]]
    output_faces[4] = [[GREEN, GREEN, GREEN], [RED, WHITE, WHITE], [RED, BLUE, BLUE]]
    # output_faces[5] should be unchanged by the rotation
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(0, 3)
    output_faces[0] = [[YELLOW, YELLOW, RED], [BLUE, BLUE, WHITE], [YELLOW, GREEN, WHITE]]
    output_faces[1] = [[YELLOW, YELLOW, GREEN], [RED, RED, RED], [ORANGE, ORANGE, WHITE]]
    output_faces[2] = [[ORANGE, GREEN, WHITE], [YELLOW, GREEN, WHITE], [BLUE, BLUE, WHITE]]
    output_faces[3] = [[ORANGE, ORANGE, BLUE], [ORANGE, ORANGE, WHITE], [RED, RED, RED]]
    output_faces[4] = [[GREEN, WHITE, BLUE], [GREEN, WHITE, BLUE], [GREEN, RED, RED]]
    # output_faces[5] should be unchanged by the rotation
    assert test_cube.compare_to(output_faces)

    # Now to test rotation on the top face
    test_cube.rotate_d(2, 1)
    output_faces[0] = [[ORANGE, ORANGE, BLUE], [BLUE, BLUE, WHITE], [YELLOW, GREEN, WHITE]]
    output_faces[1] = [[YELLOW, YELLOW, RED], [RED, RED, RED], [ORANGE, ORANGE, WHITE]]
    output_faces[2] = [[YELLOW, YELLOW, GREEN], [YELLOW, GREEN, WHITE], [BLUE, BLUE, WHITE]]
    output_faces[3] = [[ORANGE, GREEN, WHITE], [ORANGE, ORANGE, WHITE], [RED, RED, RED]]
    # output_faces[4] should be unchanged by the rotation
    output_faces[5] = [[YELLOW, BLUE, BLUE], [YELLOW, YELLOW, ORANGE], [GREEN, GREEN, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(2, 2)
    output_faces[0] = [[YELLOW, YELLOW, GREEN], [BLUE, BLUE, WHITE], [YELLOW, GREEN, WHITE]]
    output_faces[1] = [[ORANGE, GREEN, WHITE], [RED, RED, RED], [ORANGE, ORANGE, WHITE]]
    output_faces[2] = [[ORANGE, ORANGE, BLUE], [YELLOW, GREEN, WHITE], [BLUE, BLUE, WHITE]]
    output_faces[3] = [[YELLOW, YELLOW, RED], [ORANGE, ORANGE, WHITE], [RED, RED, RED]]
    # output_faces[4] should be unchanged by the rotation
    output_faces[5] = [[ORANGE, GREEN, GREEN], [ORANGE, YELLOW, YELLOW], [BLUE, BLUE, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_d(2, 3)
    output_faces[0] = [[ORANGE, GREEN, WHITE], [BLUE, BLUE, WHITE], [YELLOW, GREEN, WHITE]]
    output_faces[1] = [[ORANGE, ORANGE, BLUE], [RED, RED, RED], [ORANGE, ORANGE, WHITE]]
    output_faces[2] = [[YELLOW, YELLOW, RED], [YELLOW, GREEN, WHITE], [BLUE, BLUE, WHITE]]
    output_faces[3] = [[YELLOW, YELLOW, GREEN], [ORANGE, ORANGE, WHITE], [RED, RED, RED]]
    # output_faces[4] should be unchanged by the rotation
    output_faces[5] = [[BLUE, ORANGE, ORANGE], [BLUE, YELLOW, GREEN], [YELLOW, YELLOW, GREEN]]
    assert test_cube.compare_to(output_faces)