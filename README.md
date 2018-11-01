# customNQueenProblem
The regular Queen problem but with the option to define some unusable spaces.

This programs takes commandline arguments:
1. nqueen or nrook
  Program support working of both these types, so mention which version do you want to run.

2. Size of the board
  Designed for variable board size. 8 will create an 8x8 board.

3. Number of unavailable positions:
  Mention how many unavailable posit you want to define on the board.

4 to x. Position of the unavailable squares:
  e.g. 2 4, means the square in the 2nd row and 4th column is not available to place queen or rook.


Sample output:

1. input: python nqueen.py nqueen 8 1 1 2
Output:
_ X Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ Q _ _ _ _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
Q _ _ _ _ _ _ _

2. input: python nqueen.py nqueen 12 4 1 2 1 3 4 5 2 7 4 7
Output:
_ X X _ _ Q _ _ _ _ _ _
_ _ _ _ _ _ X Q _ _ _ _
_ _ _ _ Q _ _ _ _ _ _ _
_ _ _ _ X _ _ _ _ _ Q _
_ _ _ Q _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ Q _ _
_ _ _ _ _ _ Q _ _ _ _ _
_ _ Q _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _ _ Q
_ Q _ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ Q _ _ _
Q _ _ _ _ _ _ _ _ _ _ _
