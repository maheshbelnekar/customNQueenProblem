# customNQueensProblem
The regular [8 - Queen problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle) but with the option to define the grid size and also mark some unusable spaces.

This programs takes commandline arguments:
1. nqueen or nrook
  Program support working of both these types, so mention which version do you want to run. N-Rooks problem is bit more       relaxed than N-Queen. There's only restriction on placing maximum one rook in the same row or column.

2. Size of the board
  Designed for variable board size. 8 will create an 8x8 board.

3. Number of unavailable positions:
  Mention how many unavailable posit you want to define on the board.

4. List of unavailable positions:
  e.g. 2 4 3 2, means the squares in (2nd row, 4th column) and (3rd row,2nd column) are not available to place queen or rook.


Sample output:

1. input: python nqueen.py nqueen 8 1 1 2<br />
Output:<br />
_ X Q _ _ _ _ _<br />
_ _ _ _ _ Q _ _<br />
_ _ _ Q _ _ _ _<br />
_ Q _ _ _ _ _ _<br />
_ _ _ _ _ _ _ Q<br />
_ _ _ _ Q _ _ _<br />
_ _ _ _ _ _ Q _<br />
Q _ _ _ _ _ _ _<br />

2. input: python nqueen.py nqueen 12 4 1 2 1 3 4 5 2 7 4 7<br />
Output:<br />
_ X X _ _ Q _ _ _ _ _ <br />
_ _ _ _ _ _ X Q _ _ _ _<br />
_ _ _ _ Q _ _ _ _ _ _ _<br />
_ _ _ _ X _ _ _ _ _ Q _<br />
_ _ _ Q _ _ _ _ _ _ _ _<br />
_ _ _ _ _ _ _ _ _ Q _ _<br />
_ _ _ _ _ _ Q _ _ _ _ _<br />
_ _ Q _ _ _ _ _ _ _ _ _<br />
_ _ _ _ _ _ _ _ _ _ _ Q<br />
_ Q _ _ _ _ _ _ _ _ _ _<br />
_ _ _ _ _ _ _ _ Q _ _ _<br />
Q _ _ _ _ _ _ _ _ _ _ _<br />
