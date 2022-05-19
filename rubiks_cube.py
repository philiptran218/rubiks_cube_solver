import random
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import itertools as it
from collections import deque
from solver import *

# The following website was very helpful in understanding the use of matrices
# to create the 3D model of the cube in PyOpenGL: 
# https://stackoverflow.com/questions/50303616/how-to-rotate-slices-of-a-rubiks-cube-in-python-pyopengl

CUBE_DIM = 3
FRONT = [1, 1, 2]
BACK = [1, 1, 0]
RIGHT = [2, 1, 1]
LEFT = [0, 1, 1]
UP = [1, 2, 1]
DOWN = [1, 0, 1]

cubie_vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

cubie_edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

cubie_faces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colours = (
    (0.090, 0.631, 0.20), #Green back
    (1, 0.5, 0), #Orange left
    (0, 0, 1), #Blue front
    (0.803, 0.196, 0.196), #Red right
    (1, 1, 0), #Yellow top
    (1, 1, 1), #White bottom
)

# Maps the x, y and z orientations of colours on each cubie
cube_colours = {
    (0, 0, 0) : ["orange", "white", "green"], (0, 0, 1): ["orange", "white", None],
    (0, 0, 2) : ["orange", "white", "blue"], (0, 1, 0) : ["orange", None, "green"],
    (0, 1, 1) : ["orange", None, None], (0, 1, 2): ["orange", None, "blue"],
    (0, 2, 0) : ["orange", "yellow", "green"], (0, 2, 1) : ["orange", "yellow", None],
    (0, 2, 2) : ["orange", "yellow", "blue"], (1, 0, 0) : [None, "white", "green"],
    (1, 0, 1) : [None, "white", None], (1, 0, 2) : [None, "white", "blue"],
    (1, 1, 0) : [None, None, "green"], (1, 1, 1) : [None, None, None],
    (1, 1, 2) : [None, None, "blue"], (1, 2, 0) : [None, "yellow", "green"],
    (1, 2, 1) : [None, "yellow", None], (1, 2, 2) : [None, "yellow", "blue"],
    (2, 0, 0) : ["red", "white", "green"], (2, 0, 1) : ["red", "white", None],
    (2, 0, 2) : ["red", "white", "blue"], (2, 1, 0) : ["red", None, "green"],
    (2, 1, 1) : ["red", None, None], (2, 1, 2) : ["red", None, "blue"],
    (2, 2, 0) : ["red", "yellow", "green"], (2, 2, 1) : ["red", "yellow", None],
    (2, 2, 2) : ["red", "yellow", "blue"]
}


'''
To create rotations and cube drawings, the code uses rotation matrices and 
transformation matrices. 

Each cubie object stores its own rotation matrix and a 3D coordinate for its
intial position and current position. The rotation matrix assists in storing
the current orientation of the cubie.

Initial rotation matrix is just the identity matrix (3 lists inside another
list):

[
    [1, 0, 0]
    [0, 1, 0]
    [0, 0, 1]
]

3D coordinate is just three values inside a list which marks the position of
the cubie at the x, y and z plane. This is marked by a value from 0 to N:

(x, y, z)

Each cubie will also hold a transformation matrix, which is multiplied by a
rotation matrix when its position is changed by a rotation. The new resulting
transformation matrix is stored by the cubie.
The initial transformation matrix is made up of the rotation matrix and another
matrix which tracks the current position of the cubie:

(Using the identity matrix as the initial transformation matrix)

[
    1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    1, 1, 1, 1
    ^
    |
    The three numbers in the fourth row are the matrix coordinates of the cubie's
    current position
]

'''

# Class to create an individual cubie. A 3x3 cube will contain a list of 27
# different cubies
class cubie:
    
    # Initialises the cubie. Passes in the size of the rubik's cube, the scale
    # and the cubie's intialised position in the 3D space
    def __init__ (self, x_pos, y_pos, z_pos, size, scale):
        self.size = size
        self.scale = scale
        self.curr_pos = [x_pos, y_pos, z_pos]
        self.rot_mtx = np.identity(CUBE_DIM)
        self.trans_mtx = self.generate_trans_mtx()
        self.colours = cube_colours[(x_pos, y_pos, z_pos)]

    # Checks if the cubie will be turned by the rotation
    def is_rotated(self, axis, layer):
        return self.curr_pos[axis] == layer

    # Updates the current position and rotation matrix of a cubie when it has
    # been rotated
    def update(self, axis, layer, dir):
        if not self.is_rotated(axis, layer):
            return

        # Update the position
        swap_one = (axis + 1) % CUBE_DIM
        swap_two = (axis + 2) % CUBE_DIM
        self.curr_pos[swap_one], self.curr_pos[swap_two] = (
            self.curr_pos[swap_two] if dir < 0 else self.size - 1 - self.curr_pos[swap_two],
            self.curr_pos[swap_one] if dir > 0 else self.size - 1 - self.curr_pos[swap_one]
        )

        # Update the colours
        self.colours[swap_one], self.colours[swap_two] = self.colours[swap_two], self.colours[swap_one]

        # Update the rotation matrix
        for row in range(CUBE_DIM):
            self.rot_mtx[row][swap_one], self.rot_mtx[row][swap_two] = \
            -self.rot_mtx[row][swap_two] * dir, self.rot_mtx[row][swap_one] * dir

        # Update the transformation matrix
        self.trans_mtx = self.generate_trans_mtx()

    def generate_trans_mtx(self):
        # Multiply the rotation matrix by the scale
        rot_trans = self.rot_mtx * self.scale
        # Obtaining the scaling matrix elements for the cubes
        scale_elem = [(pos - (self.size - 1) / 2) * 2.1 * self.scale for pos in self.curr_pos]
        # Returns the computed transformation matrix for the cubie
        return [
            rot_trans[0][0], rot_trans[0][1], rot_trans[0][2], 0,
            rot_trans[1][0], rot_trans[1][1], rot_trans[1][2], 0,
            rot_trans[2][0], rot_trans[2][1], rot_trans[2][2], 0,
            scale_elem[0], scale_elem[1], scale_elem[2], 1
        ]

    # Multiplies the cubie's transformation matrix by the rotation matrix
    # to draw the rubik's cube and animate any rotations
    def generate_model(self, animate, angle, axis, layer, dir):
        glPushMatrix()
        if animate and self.is_rotated(axis, layer):
            axis_list = []
            for i in range(CUBE_DIM):
                if i == axis:
                    axis_list.append(1)
                else:
                    axis_list.append(0)
            glRotatef(angle * dir, axis_list[0], axis_list[1], axis_list[2])
        glMultMatrixf(self.trans_mtx)

        glBegin(GL_QUADS)
        for i in range(len(cubie_faces)):
            glColor3fv(colours[i])
            for j in cubie_faces[i]:
                glVertex3fv(cubie_vertices[j])
        glEnd()

        glLineWidth(4.0)
        glBegin(GL_LINES)
        for edge in cubie_edges:
            for v in edge: 
                glColor3fv((0, 0, 0))
                glVertex3fv(cubie_vertices[v])
        glEnd()
        glPopMatrix()


# Lists the keys used to rotate the entire rubik's cube object
rot_cube_dict = {
    K_UP: (-1, 0), K_DOWN: (1, 0), K_LEFT: (0, -1), K_RIGHT: (0, 1)
}

# Lists the keys used for different move rotations on the rubik's cube
moves_dict_cw = {
    K_r: (0, 2, -1), K_l: (0, 0, 1), K_m: (0, 1, 1), K_u: (1, 2, -1), 
    K_d: (1, 0, 1), K_e: (1, 1, 1), K_f: (2, 2, -1), K_b: (2, 0, 1),
    K_s: (2, 1, -1)
}

moves_dict_ccw = {
    K_r: (0, 2, 1), K_l: (0, 0, -1), K_m: (0, 1, -1), K_u: (1, 2, 1), 
    K_d: (1, 0, -1), K_e: (1, 1, -1), K_f: (2, 2, 1), K_b: (2, 0, -1),
    K_s: (2, 1, 1)
}

TURN_SPD = 5
SCRM_MOVES = 30

class rubiks_cube:

    # Initialises the entire rubik's cube object. Generates size*size*size
    # number of cubies and stores them in a list
    def __init__(self, size, scale):
        self.size = size
        self.scale = scale
        self.cubies = []
        self.undo_stack = deque()
        self.redo_stack = deque()

        for index in it.product(range(size), range(size), range(size)):
            self.cubies.append(cubie(index[0], index[1], index[2], self.size, self.scale))

        self.solver = solver(self)

    # Following methods return the colour of the centre cubie at each face of
    # the rubiks cube
    def front_colour(self):
        for cubie in self.cubies:
            if cubie.curr_pos == FRONT:
                return cubie.colours[2]

    def back_colour(self):
        for cubie in self.cubies:
            if cubie.curr_pos == BACK:
                return cubie.colours[2] 

    def right_colour(self):
        for cubie in self.cubies:
            if cubie.curr_pos == RIGHT:
                return cubie.colours[0]

    def left_colour(self):
        for cubie in self.cubies:
            if cubie.curr_pos == LEFT:
                return cubie.colours[0] 

    def up_colour(self):
        for cubie in self.cubies:
            if cubie.curr_pos == UP:
                return cubie.colours[1]

    def down_colour(self):
        for cubie in self.cubies:
            if cubie.curr_pos == DOWN:
                return cubie.colours[1] 
    
    def get_cubie(self, colours):
        for cubie in self.cubies:
            if cubie.colours.count(None) == CUBE_DIM - len(colours) and \
                all(c in cubie.colours for c in colours):
                return cubie
    
    def cubie_pos(self, pos):
        for cubie in self.cubies:
            if cubie.curr_pos == pos:
                return cubie
    
    # Checks if a given face of the rubiks cube has been solved
    def is_face_solved(self, face):
        # Have to find index where number is not 1
        index = 0
        while index < CUBE_DIM:
            if face[index] != 1:
                break 
            index += 1
        axis_1 = (index + 1) % CUBE_DIM
        axis_2 = (index + 2) % CUBE_DIM
        pos = [0, 0, 0]
        pos[index] = face[index]
        for i in it.product(range(self.size), range(self.size)):
            pos[axis_1], pos[axis_2] = i[0], i[1]
            if self.cubie_pos(pos).colours[index] != self.cubie_pos(face).colours[index]:
                return False
        return True

    # Checks if all faces of the rubiks cube has been solved
    def is_solved(self):
        return self.is_face_solved(FRONT) and self.is_face_solved(BACK) and \
            self.is_face_solved(RIGHT) and self.is_face_solved(LEFT) and \
            self.is_face_solved(UP) and self.is_face_solved(DOWN)

    # Converts key presses into rotations on the rubik's cube
    def interact(self):
        turn_x = 0
        turn_y = 0
        rot_axis = (0, 0)
        animate = False
        action = (0, 0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key in rot_cube_dict:
                        rot_axis = rot_cube_dict[event.key]
                    elif not animate and event.key in moves_dict_cw:
                        pressed_keys = pygame.key.get_pressed()
                        if pressed_keys[K_RSHIFT] or pressed_keys[K_LSHIFT]:
                            action = moves_dict_ccw[event.key]
                        else:
                            action = moves_dict_cw[event.key]
                        animate = True
                    elif event.key == K_a:
                        action = self.scramble()
                        self.clear_redo_stack()
                        self.clear_undo_stack()
                    elif event.key == K_x:
                        self.solver.solve_cube()
                    elif event.key == K_y:
                        self.redo()
                    elif event.key == K_z:
                        self.undo()
                elif event.type == KEYUP:
                    if event.key in rot_cube_dict:
                        rot_axis = (0, 0)
                elif event.type == pygame.QUIT: 
                    pygame.quit()
                    quit()  

            turn_x += rot_axis[0] * 3
            turn_y += rot_axis[1] * 3
            self.rotate_cube(turn_x, turn_y)

            if animate:
                self.undo_stack.append(action)
                self.clear_redo_stack()
            self.rotate_move(animate, action, TURN_SPD)
            animate = False

    def rotate_cube(self, turn_x, turn_y):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(0, 0, -40)
        glRotatef(turn_y, 0, 1, 0)
        glRotatef(turn_x, 1, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)  

    def rotate_move(self, animate, action, speed):
        turn_anim = 0
        if animate:
            while turn_anim < 90:
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 
                for cubie in self.cubies:
                    cubie.generate_model(animate, turn_anim, action[0], action[1], action[2])
                turn_anim += speed
                pygame.display.flip()
                pygame.time.wait(10)

            animate = False
            turn_anim = 0
            for cubie in self.cubies:    
                cubie.update(action[0], action[1], action[2])

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)  
        for cubie in self.cubies:
            cubie.generate_model(animate, turn_anim, action[0], action[1], action[2])
        pygame.display.flip()
        pygame.time.wait(10)
            
    # Scrambles the rubik's cube by performing 30 random moves    
    def scramble(self):
        for i in range(SCRM_MOVES):
            move_dir = random.randint(0, 1)
            if move_dir == 0:
                action = list(moves_dict_cw.values())[random.randint(0, 8)]
            else:
                action = list(moves_dict_ccw.values())[random.randint(0, 8)]
            
            self.rotate_move(True, action, 30)
        return action
    
    def undo(self):
        if not self.undo_stack:
            return
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        new_action = (action[0], action[1], -action[2])
        self.rotate_move(True, new_action, TURN_SPD)
    
    def clear_undo_stack(self):
        while self.undo_stack:
            self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack:
            return
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        self.rotate_move(True, action, TURN_SPD)
    
    def clear_redo_stack(self):
        while self.redo_stack:
            self.redo_stack.pop()
        
if __name__ == '__main__':
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST) 
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Can change the scale here later
    new_cube = rubiks_cube(3, 1.5)
    new_cube.interact() 
