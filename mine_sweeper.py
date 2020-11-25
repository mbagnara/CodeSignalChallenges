'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]

the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]

A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.

Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.

'''


def add_element(item):
    if item:
        return 1

    return 0


def get_total(matrix, row, col):
    summation = 0
    len_cols = len(matrix[0])
    len_rows = len(matrix)

    # test = lambda v: 1 if v else 0

    if col - 1 > -1 and row - 1 > -1:
        summation += add_element(matrix[row - 1][col - 1])

    if col - 1 > -1:
        summation += add_element(matrix[row][col - 1])

    if row + 1 < len_rows and col - 1 > -1:
        summation += add_element(matrix[row + 1][col - 1])

    if row - 1 > -1:
        summation += add_element(matrix[row - 1][col])

    if row - 1 > -1 and col + 1 < len_cols:
        summation += add_element(matrix[row - 1][col + 1])

    if row + 1 < len_rows and col + 1 < len_cols:
        summation += add_element(matrix[row + 1][col + 1])

    if col + 1 < len_cols:
        summation += add_element(matrix[row][col + 1])

    if row + 1 < len_rows:
        summation += add_element(matrix[row + 1][col])

    return summation


def minesweeper(matrix):

    new_matrix = []

    for k1, row in enumerate(matrix):

        new_list = []

        for k2, v in enumerate(row):
            t = get_total(matrix, k1, k2)
            new_list.append(t)

        new_matrix.append(new_list)

    return new_matrix


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]


matrix = [[False, False, False],
          [False, False, False]]


matrix = [[True, False, False, True],
          [False, False, True, False],
          [True, True, False, True]]


new_matrix = minesweeper(matrix)
for i in new_matrix:
    print(i)
