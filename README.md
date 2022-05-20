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

```
python rubiks_cube.py
```

The user can interact with the Rubik's Cube using certain keys on the keyboard:

- arrow keys are used to pan around the Rubik's Cube
- U, D, R, L, F, B, M, E, S are used to perform the corresponding clockwise rotations according to https://jperm.net/3x3/moves. SHIFT + Letter is to perform the corresponding counterclockwise rotation for the inputted Letter
- press A to scramble the Rubik's Cube using 30 randomised moves
- press Z to undo the most recent move
- press Y to redo the most recent undone move
- press X to solve the Rubik's Cube in its current state. Will also print out a list of moves used to solve each section

## Implementation:

### cubie

Each cubie is a representation of one of the small 27 cubes that make up the overall Rubik's Cube. They store information such as its current position list `[x, y, z]`, the orientation of its colours `[colour_x, colour_y, colour_z]`, its rotation matrix and its transformation matrix.

When a cubie is rotated, its position, colour orientation and matrices are all updated. A rotation around a certain axis will only affect the values that are not in that axis. For example, if a cubie was rotated around the x-axis, only the colours that are not in the x-axis will be swapped:

```
[colour_x, colour_y, colour_z] -> [colour_x, colour_z, colour_y]
```

The same logic is applied to the position list and the matrices, but with slight variations due to the 3D modelling.

The generate_model() method is responsible for creating the edges for the cubie and applying the colours. The cubie's transformation matrix is then used to model any animations when it is being rotated.

### rubiks_cube

The rubiks_cube class stores a list of the 27 cubies. The class is responsible for interacting with the user by accepting certain key presses.

When a rotation is performed, the rubiks_cube updates all of its cubies by checking which ones are affected by the rotation. If so, all the cubie information is updated within the cubie class, not the rubiks_cube.

The rubiks_cube also maintains a stack for undoing and redoing moves as well as a solver() class in order to move the solving logic out of the cube.

### solver

The solver is implemented using a combination of the 7 step beginner's method and the Fridrich method. The steps to solve the cube are:

1. Bottom cross
2. Bottom corners
3. Second layer edges
4. Top cross
5. Top corners
6. Permute third layer corners
7. Permute third layer edges

The Fridrich method is applied to steps 4 and 5 to reduce the number of moves for the solver. All the moves printed by the solver will solve the cube if performed from the perspective of the front face.

Links used for the solver:

The 7 step beginner's method
- https://assets.ctfassets.net/r3qu44etwf9a/6kAQCoLmbXXu29TTuArrk1/404118e1f9bfb6f9997157a284bbc572/Rubiks_Solution-Guide_3x3.pdf

The Fridrich method for OLL:
- http://badmephisto.com/oll.html

## TODO:

- Add an optimiser that can remove unnecessary moves printed by the solver function (E.g. change L L L to Li)
- Find a way to implement wide moves and whole cube rotations in just 1 move
- Provide a more robust way of accessing the cubies (potentially a dictionary with the position as the keys)
- Look into a path-searching algorithm to improve upon the solver. The solver is currently complete, but it is far from optimal

## References and Acknowledgements:

The following websites were especially helpful for suggestions on the 3D modelling, the animations and the implementation of the solver:

- https://stackoverflow.com/questions/50303616/how-to-rotate-slices-of-a-rubiks-cube-in-python-pyopengl
- https://stackoverflow.com/questions/56712877/how-do-i-render-a-matrix-as-a-cube-in-opengl?noredirect=1&lq=1
- https://github.com/pglass/cube/tree/master
- https://softwareengineering.stackexchange.com/questions/142760/how-to-represent-a-rubiks-cube-in-a-data-structure/262847#262847
- https://jperm.net/3x3/moves
- https://assets.ctfassets.net/r3qu44etwf9a/6kAQCoLmbXXu29TTuArrk1/404118e1f9bfb6f9997157a284bbc572/Rubiks_Solution-Guide_3x3.pdf
- http://badmephisto.com/oll.html
