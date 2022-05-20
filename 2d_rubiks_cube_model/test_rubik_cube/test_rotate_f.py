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

# Testing basic F rotation on the 0th layer
def test_basic_rotation_f():
    test_cube = rubiks_cube()
    test_cube.rotate_f(0, 1)
    output_faces = [0 for i in range(MAXSIZE)]
    output_faces[0] = [[BLUE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[1] = [[YELLOW, RED, RED] for i in range(ROWSIZE)]
    output_faces[2] = [[GREEN for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, ORANGE, WHITE] for i in range(ROWSIZE)]
    output_faces[4] = [[RED, RED, RED], [WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(0, 1)
    output_faces[1] = [[ORANGE, RED, RED] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, ORANGE, RED] for i in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(0, 1)
    output_faces[1] = [[WHITE, RED, RED] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, ORANGE, YELLOW] for i in range(ROWSIZE)]
    output_faces[4] = [[ORANGE, ORANGE, ORANGE], [WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW], [RED, RED, RED]]
    assert test_cube.compare_to(output_faces)

    # The cube should now be solved again
    test_cube.rotate_f(0, 1)
    assert test_cube.is_solved()

# Tests single F rotations on middle and right layer
def test_basic_rotation_f_other_layers():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]

    # Testing middle layer first (layer 1)
    test_cube.rotate_f(1, 1)
    output_faces[0] = [[BLUE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[1] = [[RED, YELLOW, RED] for i in range(ROWSIZE)]
    output_faces[2] = [[GREEN for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, WHITE, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [RED, RED, RED], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [ORANGE, ORANGE, ORANGE], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(1, 1)
    output_faces[1] = [[RED, ORANGE, RED] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, RED, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(1, 1)
    output_faces[1] = [[RED, WHITE, RED] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, YELLOW, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [ORANGE, ORANGE, ORANGE], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [RED, RED, RED], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(1, 1)
    assert test_cube.is_solved()

    # Now to test the back layer (layer 2)
    test_cube.rotate_f(2, 1)
    output_faces[1] = [[RED, RED, YELLOW] for i in range(ROWSIZE)]
    output_faces[3] = [[WHITE, ORANGE, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE], [RED, RED, RED]]
    output_faces[5] = [[ORANGE, ORANGE, ORANGE], [YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(2, 1)
    output_faces[1] = [[RED, RED, ORANGE] for i in range(ROWSIZE)]
    output_faces[3] = [[RED, ORANGE, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW]]
    output_faces[5] = [[WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(2, 1)
    output_faces[1] = [[RED, RED, WHITE] for i in range(ROWSIZE)]
    output_faces[3] = [[YELLOW, ORANGE, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE], [ORANGE, ORANGE, ORANGE]]
    output_faces[5] = [[RED, RED, RED], [YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(2, 1)
    assert test_cube.is_solved()

# Tests multiple rotations on the 0th layer
def test_multi_turns_layer_zero():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)] 
    # Testing 2 F rotations
    test_cube.rotate_f(0, 2)
    output_faces[0] = [[BLUE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[1] = [[ORANGE, RED, RED] for i in range(ROWSIZE)]
    output_faces[2] = [[GREEN for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, ORANGE, RED] for i in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(0, 3)
    output_faces[1] = [[YELLOW, RED, RED] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, ORANGE, WHITE] for i in range(ROWSIZE)]
    output_faces[4] = [[RED, RED, RED], [WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW], [ORANGE, ORANGE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(0, 4)
    assert test_cube.compare_to(output_faces)

    # Testing 5 rotations, should be equivalent to 1 rotation
    test_cube.rotate_f(0, 5)
    output_faces[1] = [[ORANGE, RED, RED] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, ORANGE, RED] for i in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE]]
    assert test_cube.compare_to(output_faces)
    
def test_multi_turns_other_layers():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]
    # Testing 2 F rotations on layer 1 first
    test_cube.rotate_f(1, 2)
    output_faces[0] = [[BLUE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[1] = [[RED, ORANGE, RED] for i in range(ROWSIZE)]
    output_faces[2] = [[GREEN for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, RED, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(1, 3)
    output_faces[1] = [[RED, YELLOW, RED] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, WHITE, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [RED, RED, RED], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [ORANGE, ORANGE, ORANGE], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(1, 4)
    assert test_cube.compare_to(output_faces)

    # Testing 5 rotations, should be equivalent to 1 rotation
    test_cube.rotate_f(1, 5)
    output_faces[1] = [[RED, ORANGE, RED] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE, RED, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    # Now testing multi rotations on layer 2
    test_cube.rotate_f(2, 2)
    output_faces[1] = [[RED, ORANGE, ORANGE] for i in range(ROWSIZE)]
    output_faces[3] = [[RED, RED, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW]]
    output_faces[5] = [[WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(2, 3)
    output_faces[1] = [[RED, ORANGE, YELLOW] for i in range(ROWSIZE)]
    output_faces[3] = [[WHITE, RED, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW], [RED, RED, RED]]
    output_faces[5] = [[ORANGE, ORANGE, ORANGE], [WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(2, 4)
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(2, 5)
    output_faces[1] = [[RED, ORANGE, ORANGE] for i in range(ROWSIZE)]
    output_faces[3] = [[RED, RED, ORANGE] for i in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW]]
    output_faces[5] = [[WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE], [YELLOW, YELLOW, YELLOW]]
    assert test_cube.compare_to(output_faces)

def test_side_layer_rotation():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]
    # Initial moves intended to scramble the front and back faces
    test_cube.rotate_r(0, 1)
    test_cube.rotate_l(1, 1)
    test_cube.rotate_u(0, 1)
    output_faces[0] = [[RED, RED, RED], [BLUE, YELLOW, WHITE], [BLUE, YELLOW, WHITE]]
    output_faces[1] = [[YELLOW, WHITE, GREEN], [RED, RED, RED], [RED, RED, RED]]
    output_faces[2] = [[ORANGE, ORANGE, ORANGE], [YELLOW, WHITE, GREEN], [YELLOW, WHITE, GREEN]]
    output_faces[3] = [[BLUE, YELLOW, WHITE], [ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE]]
    output_faces[4] = [[WHITE, BLUE, GREEN], [WHITE, BLUE, GREEN], [WHITE, BLUE, GREEN]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [GREEN, GREEN, GREEN], [BLUE, BLUE, BLUE]]
    assert test_cube.compare_to(output_faces)

    # Now use F rotations on both layers to check if front/back faces are rotating
    test_cube.rotate_f(0, 1)
    output_faces[0] = [[BLUE, BLUE, RED], [YELLOW, YELLOW, RED], [WHITE, WHITE, RED]]
    output_faces[1] = [[BLUE, WHITE, GREEN], [BLUE, RED, RED], [BLUE, RED, RED]]
    # output_faces[2] should be unchanged by the rotation
    output_faces[3] = [[BLUE, YELLOW, WHITE], [ORANGE, ORANGE, BLUE], [ORANGE, ORANGE, GREEN]]
    output_faces[4] = [[RED, RED, YELLOW], [WHITE, BLUE, GREEN], [WHITE, BLUE, GREEN]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [GREEN, GREEN, GREEN], [ORANGE, ORANGE, WHITE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(0, 2)
    output_faces[0] = [[RED, WHITE, WHITE], [RED, YELLOW, YELLOW], [RED, BLUE, BLUE]]
    output_faces[1] = [[GREEN, WHITE, GREEN], [BLUE, RED, RED], [WHITE, RED, RED]]
    # output_faces[2] should be unchanged by the rotation
    output_faces[3] = [[BLUE, YELLOW, BLUE], [ORANGE, ORANGE, BLUE], [ORANGE, ORANGE, BLUE]]
    output_faces[4] = [[WHITE, ORANGE, ORANGE], [WHITE, BLUE, GREEN], [WHITE, BLUE, GREEN]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [GREEN, GREEN, GREEN], [YELLOW, RED, RED]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(0, 3)
    output_faces[0] = [[WHITE, YELLOW, BLUE], [WHITE, YELLOW, BLUE], [RED, RED, RED]]
    output_faces[1] = [[ORANGE, WHITE, GREEN], [ORANGE, RED, RED], [WHITE, RED, RED]]
    # output_faces[2] should be unchanged by the rotation
    output_faces[3] = [[BLUE, YELLOW, RED], [ORANGE, ORANGE, RED], [ORANGE, ORANGE, YELLOW]]
    output_faces[4] = [[BLUE, BLUE, BLUE], [WHITE, BLUE, GREEN], [WHITE, BLUE, GREEN]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [GREEN, GREEN, GREEN], [GREEN, BLUE, WHITE]]
    assert test_cube.compare_to(output_faces)

    # Now to test rotation on the back face
    test_cube.rotate_f(2, 1)
    # output_faces[0] should be unchanged by the rotation
    output_faces[1] = [[ORANGE, WHITE, YELLOW], [ORANGE, RED, YELLOW], [WHITE, RED, YELLOW]]
    output_faces[2] = [[ORANGE, GREEN, GREEN], [ORANGE, WHITE, WHITE], [ORANGE, YELLOW, YELLOW]]
    output_faces[3] = [[WHITE, YELLOW, RED], [BLUE, ORANGE, RED], [GREEN, ORANGE, YELLOW]]
    output_faces[4] = [[BLUE, BLUE, BLUE], [WHITE, BLUE, GREEN], [RED, RED, GREEN]]
    output_faces[5] = [[ORANGE, ORANGE, BLUE], [GREEN, GREEN, GREEN], [GREEN, BLUE, WHITE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(2, 2)
    # output_faces[0] should be unchanged by the rotation
    output_faces[1] = [[ORANGE, WHITE, GREEN], [ORANGE, RED, BLUE], [WHITE, RED, WHITE]]
    output_faces[2] = [[YELLOW, YELLOW, ORANGE], [WHITE, WHITE, ORANGE], [GREEN, GREEN, ORANGE]]
    output_faces[3] = [[YELLOW, YELLOW, RED], [YELLOW, ORANGE, RED], [YELLOW, ORANGE, YELLOW]]
    output_faces[4] = [[BLUE, BLUE, BLUE], [WHITE, BLUE, GREEN], [BLUE, ORANGE, ORANGE]]
    output_faces[5] = [[GREEN, RED, RED], [GREEN, GREEN, GREEN], [GREEN, BLUE, WHITE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_f(2, 3)
    # output_faces[0] should be unchanged by the rotation
    output_faces[1] = [[ORANGE, WHITE, ORANGE], [ORANGE, RED, ORANGE], [WHITE, RED, BLUE]]
    output_faces[2] = [[GREEN, WHITE, YELLOW], [GREEN, WHITE, YELLOW], [ORANGE, ORANGE, ORANGE]]
    output_faces[3] = [[RED, YELLOW, RED], [RED, ORANGE, RED], [GREEN, ORANGE, YELLOW]]
    output_faces[4] = [[BLUE, BLUE, BLUE], [WHITE, BLUE, GREEN], [YELLOW, YELLOW, YELLOW]]
    output_faces[5] = [[GREEN, BLUE, WHITE], [GREEN, GREEN, GREEN], [GREEN, BLUE, WHITE]]
    assert test_cube.compare_to(output_faces)