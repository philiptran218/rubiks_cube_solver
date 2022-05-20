# Creating a cube class to represent the rubiks cube

from __future__ import print_function
# We'll use matplotlib for later to model the cube
'''
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
'''
import random 
import numpy

# Constants to help define the colours
BLUE = 0
RED = 1
GREEN = 2
ORANGE = 3
WHITE = 4
YELLOW = 5
MAXSIZE = 6
ROWSIZE = 3


class rubiks_cube:

    # Helps initiate the cube, sets all faces to their respective colours
    # Each face is a 2d array containing each cube
    def __init__(self): 
        self.face_one = [[BLUE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
        self.face_two = [[RED for i in range(ROWSIZE)] for j in range(ROWSIZE)]
        self.face_three = [[GREEN for i in range(ROWSIZE)] for j in range(ROWSIZE)]
        self.face_four = [[ORANGE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
        self.face_five = [[WHITE for i in range(ROWSIZE)] for j in range(ROWSIZE)]
        self.face_six = [[YELLOW for i in range(ROWSIZE)] for j in range(ROWSIZE)]


    # Checks if the cube has been solved
    def is_solved(self):
        if not self.is_same(self.face_one):
            return False
        if not self.is_same(self.face_two):
            return False
        if not self.is_same(self.face_three):
            return False
        if not self.is_same(self.face_four):
            return False
        if not self.is_same(self.face_five):
            return False
        if not self.is_same(self.face_six):
            return False
        return True
        

    # Checks if a face has the same colour
    def is_same(self, face):
        colour = face[0][0]
        for row in face:
            for elem in row:
                if elem != colour:
                    return False
        return True

    # Compares the rubiks cube to another cube (2d array), will return true if 
    # the two cubes are equal, false if not
    def compare_to(self, cube):
        if not numpy.array_equiv(self.face_one, cube[0]):
            return False
        if not numpy.array_equiv(self.face_two, cube[1]):
            return False
        if not numpy.array_equiv(self.face_three, cube[2]):
            return False
        if not numpy.array_equiv(self.face_four, cube[3]):
            return False
        if not numpy.array_equiv(self.face_five, cube[4]):
            return False
        if not numpy.array_equiv(self.face_six, cube[5]):
            return False
        return True
    
    
    # Different methods to rotate the cube's faces

    # Rightmost side is layer 0, all the way to leftmost face on last layer
    def rotate_r(self, layer, turns):
        for num in range(turns):
            # Creating a copy to save values before they get rotated
            copy_one = []
            copy_three = []
            copy_five = []
            copy_six = []

            for i in range(ROWSIZE):
                copy_one.append(self.face_one[i][2 - layer])
                copy_three.append(self.face_three[i][0 + layer])
                copy_five.append(self.face_five[i][2 - layer])
                copy_six.append(self.face_six[i][2 - layer])

            # Now to perform the rotation
            for i in range(ROWSIZE):
                self.face_one[i][2 - layer] = copy_five[i]
                self.face_three[i][0 + layer] = copy_six[2 - i]
                self.face_five[i][2 - layer] = copy_three[2 - i]
                self.face_six[i][2 - layer] = copy_one[i]
            
            if layer == 0:
                self.face_two = numpy.rot90(self.face_two, 3)
            elif layer == 2:
                self.face_four = numpy.rot90(self.face_four, 1)

    # Does an L turn, but uses rotate_r() to do this
    def rotate_l(self, layer, turns):
        # To filter out turns >= 4
        # 1 L turn = 3 R turns
        # 2 L turns = 2 R turns
        # 3 L turns = 1 R turn
        filter_turns = turns % 4
        if filter_turns == 1:
            filter_turns = 3
        elif filter_turns == 3:
            filter_turns = 1
        right_layer = ROWSIZE - 1 - layer
        self.rotate_r(right_layer, filter_turns)


    def rotate_f(self, layer, turns):
        for num in range(turns):
            copy_two = []
            copy_four = []
            copy_five = []
            copy_six = []

            for i in range(ROWSIZE):
                copy_two.append(self.face_two[i][0 + layer])
                copy_four.append(self.face_four[i][2 - layer])
                copy_five.append(self.face_five[0 + layer][i])
                copy_six.append(self.face_six[2 - layer][i])
        
            for i in range(ROWSIZE):
                self.face_two[i][0 + layer] = copy_six[i]
                self.face_four[i][2 - layer] = copy_five[i]
                self.face_five[0 + layer][i] = copy_two[2 - i]
                self.face_six[2 - layer][i] = copy_four[2 - i]

            if layer == 0:
                self.face_one = numpy.rot90(self.face_one, 3)
            elif layer == 2:
                self.face_three = numpy.rot90(self.face_three, 1)

    def rotate_b(self, layer, turns):
        # To filter out turns >= 4
        # 1 B turn = 3 F turns
        # 2 B turns = 2 F turns
        # 3 B turns = 1 F turn
        filter_turns = turns % 4
        if filter_turns == 1:
            filter_turns = 3
        elif filter_turns == 3:
            filter_turns = 1
        front_layer = ROWSIZE - 1 - layer
        self.rotate_f(front_layer, filter_turns)

            
    def rotate_u(self, layer, turns):
        for num in range(turns):
            copy_one = []
            copy_two = []
            copy_three = []
            copy_four = []

            for i in range(ROWSIZE):
                copy_one.append(self.face_one[0 + layer][i])
                copy_two.append(self.face_two[0 + layer][i])
                copy_three.append(self.face_three[0 + layer][i])
                copy_four.append(self.face_four[0 + layer][i])
        
            for i in range(ROWSIZE):
                self.face_one[0 + layer][i] = copy_two[i]
                self.face_two[0 + layer][i] = copy_three[i]
                self.face_three[0 + layer][i] = copy_four[i]
                self.face_four[0 + layer][i] = copy_one[i]

            if layer == 0:
                self.face_six = numpy.rot90(self.face_six, 3)
            elif layer == 2:
                self.face_five = numpy.rot90(self.face_five, 1)
    

    def rotate_d(self, layer, turns):
        # To filter out turns >= 4
        # 1 D turn = 3 U turns
        # 2 D turns = 2 U turns
        # 3 D turns = 1 U turn
        filter_turns = turns % 4
        if filter_turns == 1:
            filter_turns = 3
        elif filter_turns == 3:
            filter_turns = 1
        top_layer = ROWSIZE - 1 - layer
        self.rotate_u(top_layer, filter_turns)


    # Rotates the entire cube clockwise, 1 turn = 90 degrees clockwise
    # Axis = 1 is a horizontal turn clockwise
    # Axis = 2 is an upwards turn
    def rotate_cube(self, axis, turns):
        # To filter out turns >= 4
        num_turns = turns % 4
        for num in range(num_turns):
            if axis == 1:
                # Rotating cube clockwise is just rotating U on all layers
                # Front face becomes face no. 2, could put loop here
                self.rotate_u(0, 1)
                self.rotate_u(1, 1)
                self.rotate_u(2, 1)
            elif axis == 2:
                # Rotating cube upwards is just rotating R on all layers
                # Front face becomes face no. 5, could put loop here
                self.rotate_r(0, 1)
                self.rotate_r(1, 1)
                self.rotate_r(2, 1) 
            else:
                print("Usage error, axis argument must be 1 or 2")
                break
    
    # Scrambles the cube by 'moves' number of moves
    # R, L, F, B, U, D moves are chosen at random
    def scramble(self, moves):
        for num in range(moves):
            rand_num = random.randint(1, 6)
            rand_layer = random.randint(0, 2)
            if rand_num == 1:
                self.rotate_r(rand_layer, 1)
            elif rand_num == 2:
                self.rotate_l(rand_layer, 1)
            elif rand_num == 3:
                self.rotate_f(rand_layer, 1)
            elif rand_num == 4:
                self.rotate_b(rand_layer, 1)
            elif rand_num == 5:
                self.rotate_u(rand_layer, 1)
            elif rand_num == 6:
                self.rotate_d(rand_layer, 1)

    def perform_rotation(self, axis, layer, dir):
        # Perform an x-axis rotation (R, R', L, L', M, M')
        if axis == 0:
            if layer == 0:
                if dir == 1:
                    self.rotate_l(0, 1)
                elif dir == -1:
                    self.rotate_l(0, 3)
            if layer == 1:
                if dir == 1:
                    self.rotate_l(1, 1)
                elif dir == -1:
                    self.rotate_r(1, 1)
            if layer == 2:
                if dir == 1:
                    # 3 turns to reverse an R rotation
                    self.rotate_r(0, 3)
                elif dir == -1:
                    self.rotate_r(0, 1)

        # Perform a y-axis rotation (U, U', D, D', E, E')
        elif axis == 1:
            if layer == 0:
                if dir == 1:
                    self.rotate_d(0, 1)
                elif dir == -1:
                    self.rotate_d(0, 3)
            if layer == 1:
                if dir == 1:
                    self.rotate_d(1, 1)
                elif dir == -1:
                    self.rotate_u(1, 1)
            if layer == 2:
                if dir == 1:
                    self.rotate_u(0, 3)
                elif dir == -1:
                    self.rotate_u(0, 1)

        # Perform a z-axis rotation (F, F', B, B', S, S')
        elif axis == 2:
            if layer == 0:
                if dir == 1:
                    self.rotate_b(0, 1)
                elif dir == -1:
                    self.rotate_b(0, 3)
            if layer == 1:
                if dir == 1:
                    self.rotate_b(1, 1)
                elif dir == -1:
                    self.rotate_f(1, 1)
            if layer == 2:
                if dir == 1:
                    self.rotate_f(0, 3)
                elif dir == -1:
                    self.rotate_f(0, 1)

    # Prints the current layout of the cube (used in testing)
    def print_cube(self):
        # Now printing the top face first
        for i in range(ROWSIZE):
            print("   ", end='')
            for j in range(ROWSIZE):
                print(self.face_six[i][j], end='')
            print("\n", end ='')
        
        # Now to print the faces around the front of the cube
        for i in range(ROWSIZE):
            for j in range(ROWSIZE):
                print(self.face_four[i][j], end = '')
            for j in range(ROWSIZE):
                print(self.face_one[i][j], end = '')
            for j in range(ROWSIZE):
                print(self.face_two[i][j], end = '')
            for j in range(ROWSIZE):
                print(self.face_three[i][j], end = '')
            print("\n", end = '')
        
        # Now to print the bottom face
        for i in range(ROWSIZE):
            print("   ", end = '')
            for j in range(ROWSIZE):
                print(self.face_five[i][j], end = '')
            print("\n", end = '')
        print("")


if __name__ == "__main__":
    # Main function to be used for testing
    new_cube = rubiks_cube()
    new_cube.print_cube()
    # Yes printing should be good now
    # Assert that cube is solved
    assert new_cube.is_solved()
    # Now to test rotations
    new_cube.rotate_r(0, 2)
    new_cube.print_cube()
