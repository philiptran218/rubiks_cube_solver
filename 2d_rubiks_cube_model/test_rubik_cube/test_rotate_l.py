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

# Testing basic L rotation on the 0th layer
def test_basic_rotation_l():
    test_cube = rubiks_cube()
    test_cube.rotate_l(0, 1)
    output_faces = [0 for i in range(MAXSIZE)]
    output_faces[0] = [[YELLOW, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, WHITE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[BLUE, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[GREEN, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(0, 1)
    output_faces[0] = [[GREEN, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[WHITE, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(0, 1)
    output_faces[0] = [[WHITE, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, YELLOW] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[GREEN, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[BLUE, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    # The cube should now be solved again
    test_cube.rotate_l(0, 1)
    assert test_cube.is_solved()

# Tests single L rotations on middle and right layer
def test_basic_rotation_l_other_layers():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]

    # Testing middle layer first (layer 1)
    test_cube.rotate_l(1, 1)
    output_faces[0] = [[BLUE, YELLOW, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, WHITE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, BLUE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, GREEN, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(1, 1)
    output_faces[0] = [[BLUE, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(1, 1)
    output_faces[0] = [[BLUE, WHITE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, YELLOW, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, GREEN, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, BLUE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(1, 1)
    assert test_cube.is_solved()

    # Now to test the rightmost layer (layer 2)
    test_cube.rotate_l(2, 1)
    output_faces[0] = [[BLUE, BLUE, YELLOW] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[WHITE, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, BLUE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, GREEN] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(2, 1)
    output_faces[0] = [[BLUE, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[BLUE, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, YELLOW] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, WHITE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(2, 1)
    output_faces[0] = [[BLUE, BLUE, WHITE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[YELLOW, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, WHITE, GREEN] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, YELLOW, BLUE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(2, 1)
    assert test_cube.is_solved()

# Tests multiple rotations on the 0th layer
def test_multi_turns_layer_zero():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)] 
    # Testing 2 L rotations
    test_cube.rotate_l(0, 2)
    output_faces[0] = [[GREEN, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[WHITE, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(0, 3)
    output_faces[0] = [[YELLOW, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, WHITE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[BLUE, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[GREEN, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(0, 4)
    assert test_cube.compare_to(output_faces)

    # Testing 5 rotations, should be equivalent to 1 rotation
    test_cube.rotate_l(0, 5)
    output_faces[0] = [[GREEN, BLUE, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[YELLOW, WHITE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[WHITE, YELLOW, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)
    
def test_multi_turns_other_layers():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]
    # Testing 2 L rotations on layer 1 first
    test_cube.rotate_l(1, 2)
    output_faces[0] = [[BLUE, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(1, 3)
    output_faces[0] = [[BLUE, YELLOW, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, WHITE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, BLUE, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, GREEN, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(1, 4)
    assert test_cube.compare_to(output_faces)

    # Testing 5 rotations, should be equivalent to 1 rotation
    test_cube.rotate_l(1, 5)
    output_faces[0] = [[BLUE, GREEN, BLUE] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[GREEN, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, WHITE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, YELLOW] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    # Now testing multi rotations on layer 2
    test_cube.rotate_l(2, 2)
    output_faces[0] = [[BLUE, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[BLUE, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, YELLOW] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, WHITE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(2, 3)
    output_faces[0] = [[BLUE, GREEN, YELLOW] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[WHITE, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, BLUE] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, GREEN] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(2, 4)
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(2, 5)
    output_faces[0] = [[BLUE, GREEN, GREEN] for i in range(ROWSIZE)]
    output_faces[1] = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[2] = [[BLUE, BLUE, GREEN] for i in range(ROWSIZE)]
    output_faces[3] = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
    output_faces[4] = [[WHITE, YELLOW, YELLOW] for i in range(ROWSIZE)]
    output_faces[5] = [[YELLOW, WHITE, WHITE] for i in range(ROWSIZE)]
    assert test_cube.compare_to(output_faces)

def test_side_layer_rotation():
    test_cube = rubiks_cube()
    output_faces = [0 for i in range(MAXSIZE)]
    # Initial moves intended to scramble the right and left faces
    test_cube.rotate_r(0, 1)
    test_cube.rotate_f(0, 1)
    test_cube.rotate_u(0, 1)
    output_faces[0] = [[YELLOW, RED, RED], [BLUE, BLUE, BLUE], [WHITE, WHITE, WHITE]]
    output_faces[1] = [[YELLOW, GREEN, GREEN], [YELLOW, RED, RED], [BLUE, RED, RED]]
    output_faces[2] = [[ORANGE, ORANGE, WHITE], [YELLOW, GREEN, GREEN], [YELLOW, GREEN, GREEN]]
    output_faces[3] = [[BLUE, BLUE, BLUE], [ORANGE, ORANGE, WHITE], [ORANGE, ORANGE, GREEN]]
    output_faces[4] = [[RED, RED, RED], [WHITE, WHITE, GREEN], [WHITE, WHITE, GREEN]]
    output_faces[5] = [[ORANGE, YELLOW, YELLOW], [ORANGE, YELLOW, YELLOW], [ORANGE, BLUE, BLUE]]
    assert test_cube.compare_to(output_faces)

    # Now use L rotations on both layers to check if side faces are rotating
    test_cube.rotate_l(0, 1)
    output_faces[0] = [[ORANGE, RED, RED], [ORANGE, BLUE, BLUE], [ORANGE, WHITE, WHITE]]
    # output_faces[1] should be unchanged by the rotation
    output_faces[2] = [[ORANGE, ORANGE, WHITE], [YELLOW, GREEN, WHITE], [YELLOW, GREEN, RED]]
    output_faces[3] = [[ORANGE, ORANGE, BLUE], [ORANGE, ORANGE, BLUE], [GREEN, WHITE, BLUE]]
    output_faces[4] = [[YELLOW, RED, RED], [BLUE, WHITE, GREEN], [WHITE, WHITE, GREEN]]
    output_faces[5] = [[GREEN, YELLOW, YELLOW], [GREEN, YELLOW, YELLOW], [WHITE, BLUE, BLUE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(0, 2)
    output_faces[0] = [[RED, RED, RED], [WHITE, BLUE, BLUE], [WHITE, WHITE, WHITE]]
    # output_faces[1] should be unchanged by the rotation
    output_faces[2] = [[ORANGE, ORANGE, ORANGE], [YELLOW, GREEN, ORANGE], [YELLOW, GREEN, ORANGE]]
    output_faces[3] = [[BLUE, WHITE, GREEN], [BLUE, ORANGE, ORANGE], [BLUE, ORANGE, ORANGE]]
    output_faces[4] = [[GREEN, RED, RED], [GREEN, WHITE, GREEN], [WHITE, WHITE, GREEN]]
    output_faces[5] = [[YELLOW, YELLOW, YELLOW], [BLUE, YELLOW, YELLOW], [WHITE, BLUE, BLUE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(0, 3)
    output_faces[0] = [[GREEN, RED, RED], [GREEN, BLUE, BLUE], [WHITE, WHITE, WHITE]]
    # output_faces[1] should be unchanged by the rotation
    output_faces[2] = [[ORANGE, ORANGE, WHITE], [YELLOW, GREEN, BLUE], [YELLOW, GREEN, YELLOW]]
    output_faces[3] = [[GREEN, ORANGE, ORANGE], [WHITE, ORANGE, ORANGE], [BLUE, BLUE, BLUE]]
    output_faces[4] = [[ORANGE, RED, RED], [ORANGE, WHITE, GREEN], [ORANGE, WHITE, GREEN]]
    output_faces[5] = [[RED, YELLOW, YELLOW], [WHITE, YELLOW, YELLOW], [WHITE, BLUE, BLUE]]
    assert test_cube.compare_to(output_faces)

    # Now to test rotation on the right face
    test_cube.rotate_l(2, 1)
    output_faces[0] = [[GREEN, RED, YELLOW], [GREEN, BLUE, YELLOW], [WHITE, WHITE, BLUE]]
    output_faces[1] = [[GREEN, RED, RED], [GREEN, RED, RED], [YELLOW, YELLOW, BLUE]]
    output_faces[2] = [[GREEN, ORANGE, WHITE], [GREEN, GREEN, BLUE], [RED, GREEN, YELLOW]]
    # output_faces[3] should be unchanged by the rotation
    output_faces[4] = [[ORANGE, RED, RED], [ORANGE, WHITE, BLUE], [ORANGE, WHITE, WHITE]]
    output_faces[5] = [[RED, YELLOW, YELLOW], [WHITE, YELLOW, YELLOW], [WHITE, BLUE, ORANGE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(2, 2)
    output_faces[0] = [[GREEN, RED, RED], [GREEN, BLUE, GREEN], [WHITE, WHITE, GREEN]]
    output_faces[1] = [[BLUE, YELLOW, YELLOW], [RED, RED, GREEN], [RED, RED, GREEN]]
    output_faces[2] = [[BLUE, ORANGE, WHITE], [YELLOW, GREEN, BLUE], [YELLOW, GREEN, YELLOW]]
    # output_faces[3] should be unchanged by the rotation
    output_faces[4] = [[ORANGE, RED, YELLOW], [ORANGE, WHITE, YELLOW], [ORANGE, WHITE, ORANGE]]
    output_faces[5] = [[RED, YELLOW, RED], [WHITE, YELLOW, BLUE], [WHITE, BLUE, WHITE]]
    assert test_cube.compare_to(output_faces)

    test_cube.rotate_l(2, 3)
    output_faces[0] = [[GREEN, RED, YELLOW], [GREEN, BLUE, YELLOW], [WHITE, WHITE, ORANGE]]
    output_faces[1] = [[RED, RED, BLUE], [RED, RED, YELLOW], [GREEN, GREEN, YELLOW]]
    output_faces[2] = [[WHITE, ORANGE, WHITE], [BLUE, GREEN, BLUE], [RED, GREEN, YELLOW]]
    # output_faces[3] should be unchanged by the rotation
    output_faces[4] = [[ORANGE, RED, YELLOW], [ORANGE, WHITE, YELLOW], [ORANGE, WHITE, BLUE]]
    output_faces[5] = [[RED, YELLOW, RED], [WHITE, YELLOW, GREEN], [WHITE, BLUE, GREEN]]
    assert test_cube.compare_to(output_faces)
    