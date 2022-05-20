# rubiks_cube_solver

This is an implementation of a 3x3 Rubik's Cube in Python.

The Interactive Rubik's Cube contains the following features:

- A 3D model of the Rubik's Cube comprised of 27 smaller 'cubies'
- A scrambler that randomises the cube using 30 different rotations
- An undo and redo function to reverse unwanted rotations
- A solver that is a mix of the 7 step beginner's method and the Fridrich method

## How to use the Rubik's Cube:

To run the application, an installation of Pygame and OpenGL is required.

Running the following command should successfully run the application:
'''
python rubiks_cube.py
'''
The user can interact with the Rubik's Cube using certain keys on the keyboard:

- arrow keys are used to pan around the Rubik's Cube
- U, D, R, L, F, B, M, E, S are used to perform the corresponding clockwise rotations according to https://jperm.net/3x3/moves. SHIFT + Letter is to perform the corresponding counterclockwise rotation for the inputted Letter
- press A to scramble the Rubik's Cube using 30 randomised moves
- press Z to undo the most recent move
- press Y to redo the most recent undone move
- press X to solve the Rubik's Cube in its current state. Will also print out a list of moves used to solve each section

## Implementation:


## TODO:

- Add an optimiser that can remove unnecessary moves printed by the solver function (E.g. change L L L to Li)
- Provide a more robust way of accessing the cubies (potentially a dictionary with the position as the keys)
- Look into a path-searching algorithm to improve upon the solver. The solver is currently complete, but it is far from optimal

## References and Acknowledgements:



