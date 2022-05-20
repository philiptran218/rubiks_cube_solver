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
