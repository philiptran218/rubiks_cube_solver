# Solving algorithm for the 3x3 rubiks cube

'''
Ideas:

Instead of using a matrix to track the orientation of colours in the visual_cube
representation, could instead use rubiks_cube.py matrix instead. When a move is
performed on the visual_cube, match the same moves onto the rubiks_cube array as
well. This way, it will give a representation of the colours on the cube.

Use the rubiks_cube representation to track colours to check goals and assert
when the cube has been solved.

May have to solve this using a beginner's method (White cross, white corners,
second layer, yellow top and permute remaining layer). Have to include different
methods and goals in order to achieve this. 

After this is done, might choose to optimise the solver or move onto implementing
path searching algorithms.
'''

CUBE_DIM = 3
NUM_STEPS = 7
SOLVE_SPD = 20
FRONT = [1, 1, 2]
BACK = [1, 1, 0]
RIGHT = [2, 1, 1]
LEFT = [0, 1, 1]
UP = [1, 2, 1]
DOWN = [1, 0, 1]

moves_dict = {
    "R": (0, 2, -1), "L": (0, 0, 1), "M": (0, 1, 1), "U": (1, 2, -1), 
    "D": (1, 0, 1), "E": (1, 1, 1), "F": (2, 2, -1), "B": (2, 0, 1),
    "S": (2, 1, -1),
    "Ri": (0, 2, 1), "Li": (0, 0, -1), "Mi": (0, 1, -1), "Ui": (1, 2, 1), 
    "Di": (1, 0, -1), "Ei": (1, 1, -1), "Fi": (2, 2, 1), "Bi": (2, 0, -1),
    "Si": (2, 1, 1)
}

class solver:

    # Stub code for now
    def __init__(self, cube):
        self.cube = cube
        self.moves = self.initialise_moves_list()

    def initialise_moves_list(self):
        return [[] for _ in range(NUM_STEPS)]

    # Have to change these to map actual rotations later. Have to return the
    # corresponding action tuple for the rotation
    def get_face_rot(self, face):
        if face == RIGHT:
            return "R", "Ri"
        elif face == LEFT:
            return "L", "Li"
        elif face == FRONT:
            return "F", "Fi"
        elif face == BACK:
            return "B", "Bi"
        elif face == UP:
            return "U", "Ui"
        elif face == DOWN:
            return "D", "Di"

    # Records the move(s) into a list and performs the rotation on the rubiks cube
    def record_move(self, moves_list, step_num):
        # Add new moves to the existing moves list
        self.moves[step_num] = self.moves[step_num] + moves_list
        for move in moves_list:
            self.cube.rotate_move(True, moves_dict[move], SOLVE_SPD)

    def solve_cube(self):
        self.moves = self.initialise_moves_list()
        print("Moves to solve the bottom cross:")
        self.cross()
        print(self.moves[0])
        print("Moves to solve the bottom corners:")
        self.cross_corners()
        print(self.moves[1])
        print("Moves to solve the middle layer:")
        self.middle_layer()
        print(self.moves[2])
        print("Moves to solve the top cross:")
        self.top_cross()
        print(self.moves[3])
        print("Moves to solve the top corners:")
        self.top_cross_corner()
        print(self.moves[4])
        print("Moves to permute the final layer corners:")
        self.permute_corners()
        print(self.moves[5])
        print("Moves to permute the final layer edges:")
        self.permute_edges()
        print(self.moves[6])
        print("Rubiks cube has been solved!")

    # Create the cross on the bottom layer of the cube
    def cross(self):
        # Obtain the edge cubies that need to be placed into the cross
        r_cubie = self.cube.get_cubie([self.cube.down_colour(), self.cube.right_colour()])
        l_cubie = self.cube.get_cubie([self.cube.down_colour(), self.cube.left_colour()])
        f_cubie = self.cube.get_cubie([self.cube.down_colour(), self.cube.front_colour()])
        b_cubie = self.cube.get_cubie([self.cube.down_colour(), self.cube.back_colour()])

        self.left_right_cross(l_cubie, self.cube.get_cubie([self.cube.left_colour()]),
        ["L", "L"], ["Si", "L", "S", "Li"])

        self.left_right_cross(r_cubie, self.cube.get_cubie([self.cube.right_colour()]),
        ["R", "R"], ["S", "R", "Si", "Ri"])

        self.record_move(["U", "Ei", "Di"], 0)

        self.left_right_cross(f_cubie, self.cube.get_cubie([self.cube.left_colour()]),
        ["L", "L"], ["Si", "L", "S", "Li"])

        self.left_right_cross(b_cubie, self.cube.get_cubie([self.cube.right_colour()]),
        ["R", "R"], ["S", "R", "Si", "Ri"])

        self.record_move(["Ui", "E", "D"], 0)

    
    def left_right_cross(self, edge_cubie, centre_cubie, move_1, move_2):
        # Check if in correct position
        if self.is_in_cross(edge_cubie, centre_cubie):
            return

        # If not, ideally want to move cubie to y=2 layer, so it can be slotted
        # into the cross
        # If cubie is currently in y=1 layer
        undo_move = []

        if edge_cubie.curr_pos[1] == 1:
            pos = []
            pos.append(1)
            pos.append(edge_cubie.curr_pos[1])
            pos.append(edge_cubie.curr_pos[2])
            cw_move, ccw_move = self.get_face_rot(pos)
            
            if edge_cubie.curr_pos == [2, 1, 0] or edge_cubie.curr_pos == [0, 1, 2]:
                self.record_move([cw_move], 0)
                undo_move.append(ccw_move)
            else:
                self.record_move([ccw_move], 0)
                undo_move.append(cw_move)

        # If cubie is stranded in y=0 layer
        elif edge_cubie.curr_pos[1] == 0:
            pos = []
            pos.append(edge_cubie.curr_pos[0])
            pos.append(1)
            pos.append(edge_cubie.curr_pos[2])
            cw_move, ccw_move = self.get_face_rot(pos)

            # Perform double rotation for ccw_move
            self.record_move([ccw_move, ccw_move], 0)

            if edge_cubie.curr_pos[2] != centre_cubie.curr_pos[2]:
                # Set undo_move to be a double rotation of cw_move
                undo_move.append(cw_move)
                undo_move.append(cw_move)
        
        # At this point, the cubie should now be in the y=2 layer
        # Once cubie is in y=2 layer, can slot it into the cross

        error_count = 0
        while [edge_cubie.curr_pos[0], edge_cubie.curr_pos[2]] != [centre_cubie.curr_pos[0], centre_cubie.curr_pos[2]]:
            # Keep performing U rotation here until satisfied
            self.record_move(["U"], 0)
            error_count += 1
            if error_count > 10:
                print("Cannot solve this cube!")

        self.record_move(undo_move, 0)

        if edge_cubie.colours[0] == centre_cubie.colours[0]:
            self.record_move(move_1, 0)
        else:
            self.record_move(move_2, 0)

    def is_in_cross(self, edge_cubie, centre_cubie):
        pos = centre_cubie.curr_pos
        return edge_cubie.colours[1] == self.cube.down_colour() and \
            edge_cubie.curr_pos == [pos[0], 0, pos[2]]
    
    # Inserts the corner pieces into the cross on the bottom layer
    def cross_corners(self):
        fr_cubie = self.cube.get_cubie([self.cube.front_colour(), self.cube.right_colour(), self.cube.down_colour()])
        fl_cubie = self.cube.get_cubie([self.cube.front_colour(), self.cube.left_colour(), self.cube.down_colour()])
        br_cubie = self.cube.get_cubie([self.cube.back_colour(), self.cube.right_colour(), self.cube.down_colour()])
        bl_cubie = self.cube.get_cubie([self.cube.back_colour(), self.cube.left_colour(), self.cube.down_colour()])

        self.slot_corners(fr_cubie, self.cube.get_cubie([self.cube.front_colour()]),
        self.cube.get_cubie([self.cube.right_colour()]))

        self.slot_corners(br_cubie, self.cube.get_cubie([self.cube.front_colour()]),
        self.cube.get_cubie([self.cube.right_colour()]))

        self.slot_corners(bl_cubie, self.cube.get_cubie([self.cube.front_colour()]),
        self.cube.get_cubie([self.cube.right_colour()]))

        self.slot_corners(fl_cubie, self.cube.get_cubie([self.cube.front_colour()]),
        self.cube.get_cubie([self.cube.right_colour()]))

    def slot_corners(self, corner_cubie, front_cubie, right_cubie):
        # Check if the corner cube is already in the correct position with the
        # correct colour orientation
        if self.is_in_corner(corner_cubie):
            self.record_move(["U", "Ei", "Di"], 1)
            return
        
        # If corner is on y=0 layer, have to move it back into the y=2 layer
        if corner_cubie.curr_pos[1] == 0:
            pos = []
            pos.append(corner_cubie.curr_pos[0])
            pos.append(1)
            pos.append(1)
            cw_move, ccw_move = self.get_face_rot(pos)

            if corner_cubie.curr_pos == [2, 0, 2] or corner_cubie.curr_pos == [0, 0, 0]:
                self.record_move([cw_move, "U", ccw_move], 1)
            else:
                self.record_move([ccw_move, "U", cw_move], 1)

        # Keep looping corner piece until it aligns with the front-right corner
        while [corner_cubie.curr_pos[0], corner_cubie.curr_pos[2]] != [right_cubie.curr_pos[0], front_cubie.curr_pos[2]]:
            # Keep performing U rotations
            self.record_move(["U"], 1)

        # Now have to perform moves depending on the orientation of the bottom
        # colour on the corner cubie
        # If down colour is facing the right
        if corner_cubie.colours[0] == self.cube.down_colour():
            moves = ["R", "U", "Ri"]
        # If down colour is facing upwards
        elif corner_cubie.colours[1] == self.cube.down_colour():
            moves = ["Fi", "U", "F", "U", "U", "Fi", "Ui", "F"]
        # If down colour is facing forwards
        else:
            moves = ["Fi", "Ui", "F"]
        
        self.record_move(moves, 1)
        self.record_move(["U", "Ei", "Di"], 1)

    def is_in_corner(self, corner_cubie):
        pos = corner_cubie.curr_pos
        return corner_cubie.colours[0] == self.cube.right_colour() and \
            corner_cubie.colours[2] == self.cube.front_colour() and \
            pos == [2, 0, 2]

    # Slots the edge cubies into correct positions above the corner cubies
    def middle_layer(self):
        fr_cubie = self.cube.get_cubie([self.cube.front_colour(), self.cube.right_colour()])
        fl_cubie = self.cube.get_cubie([self.cube.front_colour(), self.cube.left_colour()])
        br_cubie = self.cube.get_cubie([self.cube.back_colour(), self.cube.right_colour()])
        bl_cubie = self.cube.get_cubie([self.cube.back_colour(), self.cube.left_colour()])

        self.slot_side_cubes(fr_cubie)
        self.slot_side_cubes(fl_cubie)
        self.slot_side_cubes(br_cubie)
        self.slot_side_cubes(bl_cubie)

    def slot_side_cubes(self, edge_cubie):
        # Check if edge cubie is already in correct position
        if self.is_in_edge(edge_cubie):
            return
        
        # If edge cubie is stuck in the y=1 layer, have to move it to y=2 layer
        if edge_cubie.curr_pos[1] == 1:
            while [edge_cubie.curr_pos[0], edge_cubie.curr_pos[2]] != [2, 2]:
                self.record_move(["Ei", "Di"], 2)
            
            self.record_move(["U", "R", "Ui", "Ri", "Ui", "Fi", "U", "F"], 2)

        # When cubie is in y=2 layer, can rotate and insert it into correct spot
        # Want to bring the edge_cubie to the front on the cube
        while [edge_cubie.curr_pos[0], edge_cubie.curr_pos[2]] != [1, 2]:
            self.record_move(["U"], 2)
        
        while edge_cubie.colours[2] != self.cube.front_colour():
            self.record_move(["Ei", "Di"], 2)
        
        if edge_cubie.colours[1] == self.cube.left_colour():
            moves = ["Ui", "Li", "U", "L", "U", "F", "Ui", "Fi"]
        else:
            moves = ["U", "R", "Ui", "Ri", "Ui", "Fi", "U", "F"]

        self.record_move(moves, 2)

    def is_in_edge(self, edge_cubie):
        pos = edge_cubie.curr_pos
        colours = edge_cubie.colours
        if pos == [2, 1, 2] and colours[0] == self.cube.right_colour() and \
            colours[2] == self.cube.front_colour():
            return True
        elif pos == [2, 1, 0] and colours[0] == self.cube.right_colour() and \
            colours[2] == self.cube.back_colour():
            return True
        elif pos == [0, 1, 2] and colours[0] == self.cube.left_colour() and \
            colours[2] == self.cube.front_colour():
            return True
        elif pos == [0, 1, 0] and colours[0] == self.cube.left_colour() and \
            colours[2] == self.cube.back_colour():
            return True
        else:
            return False

    def top_cross(self):
        # Have to check when the cube will create the yellow cross
        colour = self.cube.up_colour()
        count = 0
        moves = []
        while not self.cross_complete(colour):
            if self.top_line(colour):
                moves = ["F", "R", "U", "Ri", "Ui", "Fi"]
                break
            elif self.top_L(colour):
                moves = ["F", "S", "R", "U", "Ri", "Ui", "Si", "Fi"]
                break
            self.record_move(["U"], 3)
            count += 1

            if count == 4:
                self.record_move(["F", "S", "R", "U", "Ri", "Ui", "Si", "Fi"], 3)
        
        self.record_move(moves, 3)

    def top_L(self, colour):
        return self.cube.cubie_pos([1, 2, 2]).colours[1] == colour and \
            self.cube.cubie_pos([2, 2, 1]).colours[1] == colour

    def top_line(self, colour):
        return self.cube.cubie_pos([0, 2, 1]).colours[1] == colour and \
            self.cube.cubie_pos([2, 2, 1]).colours[1] == colour

    def cross_complete(self, colour):
        return self.cube.cubie_pos([1, 2, 0]).colours[1] == colour and \
            self.cube.cubie_pos([0, 2, 1]).colours[1] == colour and \
            self.cube.cubie_pos([2, 2, 1]).colours[1] == colour and \
            self.cube.cubie_pos([1, 2, 2]).colours[1] == colour

    # Now will solve the colours for the top face
    def top_cross_corner(self):
        # This method will use the Fridrich method to quickly solve the top face
        # Will perform moves based on 7 different possible cases for top face
        colour = self.cube.up_colour()
        moves = []
        while not self.top_layer_complete(colour):
            if self.top_case_1(colour):
                moves = ["F", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "Fi"]
                break
            elif self.top_case_2(colour):
                moves = ["R", "Ui", "Ui", "Ri", "Ri", "Ui", "R", "R", "Ui", "Ri", "Ri", "U", "U", "R"]
                break
            elif self.top_case_3(colour):
                moves = ["R", "Mi", "U", "Ri", "Ui", "Ri", "M", "F", "R", "Fi"]
                break
            elif self.top_case_4(colour):
                moves = ["Fi", "R", "Mi", "U", "Ri", "Ui", "Ri", "M", "F", "R"]
                break
            elif self.top_case_5(colour):
                moves = ["R", "U", "Ri", "U", "R", "U", "U", "Ri"]
                break
            elif self.top_case_6(colour):
                moves = ["R", "U", "U", "Ri", "Ui", "R", "Ui", "Ri"]
                break
            elif self.top_case_7(colour):
                moves = ["R", "R", "D", "Ri", "U", "U", "R", "Di", "Ri", "U", "U", "Ri"]
                break
            else:
                self.record_move(["U"], 4)
        
        self.record_move(moves, 4)

    # See http://badmephisto.com/oll.html for the cases outlined below
    # Don't have to specify positions for cross, we already know it's there
    # Case 3
    def top_case_1(self, colour):
        return self.cube.cubie_pos([0, 2, 0]).colours[2] == colour and \
            self.cube.cubie_pos([2, 2, 0]).colours[2] == colour and \
            self.cube.cubie_pos([0, 2, 2]).colours[2] == colour and \
            self.cube.cubie_pos([2, 2, 2]).colours[2] == colour
    
    # Case 13
    def top_case_2(self, colour):
        return self.cube.cubie_pos([0, 2, 0]).colours[0] == colour and \
            self.cube.cubie_pos([2, 2, 0]).colours[2] == colour and \
            self.cube.cubie_pos([0, 2, 2]).colours[0] == colour and \
            self.cube.cubie_pos([2, 2, 2]).colours[2] == colour
    
    # Case 21
    def top_case_3(self, colour):
        return self.cube.cubie_pos([0, 2, 0]).colours[2] == colour and \
            self.cube.cubie_pos([2, 2, 0]).colours[1] == colour and \
            self.cube.cubie_pos([0, 2, 2]).colours[2] == colour and \
            self.cube.cubie_pos([2, 2, 2]).colours[1] == colour
    
    # Case 22
    def top_case_4(self, colour):
        return self.cube.cubie_pos([0, 2, 0]).colours[0] == colour and \
            self.cube.cubie_pos([2, 2, 0]).colours[1] == colour and \
            self.cube.cubie_pos([0, 2, 2]).colours[1] == colour and \
            self.cube.cubie_pos([2, 2, 2]).colours[2] == colour

    # Case 35
    def top_case_5(self, colour):
        return self.cube.cubie_pos([0, 2, 0]).colours[2] == colour and \
            self.cube.cubie_pos([2, 2, 0]).colours[0] == colour and \
            self.cube.cubie_pos([0, 2, 2]).colours[1] == colour and \
            self.cube.cubie_pos([2, 2, 2]).colours[2] == colour
    
    # Case 36
    def top_case_6(self, colour):
        return self.cube.cubie_pos([0, 2, 0]).colours[0] == colour and \
            self.cube.cubie_pos([2, 2, 0]).colours[1] == colour and \
            self.cube.cubie_pos([0, 2, 2]).colours[2] == colour and \
            self.cube.cubie_pos([2, 2, 2]).colours[0] == colour

    # Case 48
    def top_case_7(self, colour):
        return self.cube.cubie_pos([0, 2, 0]).colours[1] == colour and \
            self.cube.cubie_pos([2, 2, 0]).colours[1] == colour and \
            self.cube.cubie_pos([0, 2, 2]).colours[2] == colour and \
            self.cube.cubie_pos([2, 2, 2]).colours[2] == colour
    
    def top_layer_complete(self, colour):
        return self.cube.cubie_pos([0, 2, 0]).colours[1] == colour and \
            self.cube.cubie_pos([2, 2, 1]).colours[1] == colour and \
            self.cube.cubie_pos([0, 2, 2]).colours[1] == colour and \
            self.cube.cubie_pos([2, 2, 2]).colours[1] == colour
    
    # Method will move the top corners into the correct positions
    def permute_corners(self):
        moves = ["Ri", "F", "Ri", "B", "B", "R", "Fi", "Ri", "B", "B", "R", "R", "Ui"]
        while not self.corners_complete():
            # If back corners are present, just keeping rotating cube until the face
            # becomes the back face 
            if self.same_back_corners():
                while self.cube.cubie_pos([0, 2, 0]).colours[2] != self.cube.cubie_pos([2, 2, 0]).colours[2]:
                    self.record_move(["U"], 5)
                while self.cube.back_colour() != self.cube.cubie_pos([0, 2, 0]).colours[2]:
                    self.record_move(["Ei", "Di"], 5)
            # Otherwise, it must have two same diagonal corners, just have to keep
            # rotating until the corners align
            else: 
                while not self.diagonal_corners_complete():
                    self.record_move(["U"], 5)

            self.record_move(moves, 5)
            
    def same_back_corners(self):
        return self.cube.cubie_pos([0, 2, 0]).colours[2] == self.cube.cubie_pos([2, 2, 0]).colours[2] or \
            self.cube.cubie_pos([2, 2, 0]).colours[0] == self.cube.cubie_pos([2, 2, 2]).colours[0] or \
            self.cube.cubie_pos([2, 2, 2]).colours[2] == self.cube.cubie_pos([0, 2, 2]).colours[2] or \
            self.cube.cubie_pos([0, 2, 0]).colours[0] == self.cube.cubie_pos([0, 2, 2]).colours[0]

    def diagonal_corners_complete(self):
        return (self.cube.cubie_pos([0, 2, 0]).colours[0] == self.cube.left_colour() and \
            self.cube.cubie_pos([0, 2, 0]).colours[2] == self.cube.back_colour() and \
            self.cube.cubie_pos([2, 2, 2]).colours[0] == self.cube.right_colour() and \
            self.cube.cubie_pos([2, 2, 2]).colours[2] == self.cube.front_colour()) or \
            (self.cube.cubie_pos([2, 2, 0]).colours[0] == self.cube.right_colour() and \
            self.cube.cubie_pos([2, 2, 0]).colours[2] == self.cube.back_colour() and \
            self.cube.cubie_pos([0, 2, 2]).colours[0] == self.cube.left_colour() and \
            self.cube.cubie_pos([0, 2, 2]).colours[2] == self.cube.front_colour())

    def corners_complete(self):
        count = 0
        while count < 4:
            if self.cube.cubie_pos([0, 2, 0]).colours[0] == self.cube.left_colour() and \
                self.cube.cubie_pos([0, 2, 0]).colours[2] == self.cube.back_colour() and \
                self.cube.cubie_pos([2, 2, 0]).colours[0] == self.cube.right_colour() and \
                self.cube.cubie_pos([2, 2, 0]).colours[2] == self.cube.back_colour() and \
                self.cube.cubie_pos([0, 2, 2]).colours[0] == self.cube.left_colour() and \
                self.cube.cubie_pos([0, 2, 2]).colours[2] == self.cube.front_colour() and \
                self.cube.cubie_pos([2, 2, 2]).colours[0] == self.cube.right_colour() and \
                self.cube.cubie_pos([2, 2, 2]).colours[2] == self.cube.front_colour():
                return True
            else:
                self.record_move(["U"], 5)
                count += 1
        return False
    
    # This is the final step. Now have to insert the edge cubies into the correct
    # positions
    def permute_edges(self):
        moves = ["F", "F", "U", "L", "Ri", "F", "F", "Li", "R", "U", "F", "F"]
        while not self.cube.is_solved():
            # This line is here to fix the corners if it has been rearranged
            self.corners_complete()
            # Have to check if there is a solved face (don't have to check BACK)
            if self.cube.is_face_solved(FRONT) or self.cube.is_face_solved(RIGHT) or \
                self.cube.is_face_solved(LEFT):
                while not self.cube.is_face_solved(BACK):
                    self.record_move(["U", "Ei", "Di"], 6)
                
            self.record_move(moves, 6)
