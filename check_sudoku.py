def check_sudoku(sudoku):

    from check_sudoku_cuadrado import check_sudoku_cuadrado
    from check_numbers_in_range import check_numbers_in_range
    from check_rows_in_sudoku import check_rows_in_sudoku
    from check_columns_in_sudoku import check_columns_in_sudoku

    return check_sudoku_cuadrado(sudoku) and check_numbers_in_range(sudoku) and check_rows_in_sudoku(sudoku) and check_columns_in_sudoku(sudoku)


if __name__ == '__main__':
    assert check_sudoku([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, 2]]) == True
    assert check_sudoku([[1, 2, 3, 4],
                        [2, 3, 1, 3],
                        [3, 1, 2, 3],
                        [4, 4, 4, 4]]) == False
    assert check_sudoku([[1, 2, 3, 4],
                        [2, 3, 1, 4],
                        [4, 1, 2, 3],
                        [3, 4, 1, 2]]) == False
    assert check_sudoku([[1, 2, 3, 4, 5],
                        [2, 3, 1, 5, 6],
                        [4, 5, 2, 1, 3],
                        [3, 4, 5, 2, 1],
                        [5, 6, 4, 3, 2]]) == False
    assert check_sudoku([[1, 2, 3, 4, 5],
                        [2, 3, 1, 5, 6],
                        [4, 5, 2, 1, 3],
                        [3, 4, 5, 2, 1],
                        [5, 6, 4, 3, 2]]) == False
    assert check_sudoku([['a', 'b', 'c'],
                        ['b', 'c', 'a'],
                        ['c', 'a', 'b']]) == False
    assert check_sudoku([[1, 1.5],
                        [1.5, 1]]) == False
    assert check_sudoku([[1, 0, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0, 1]]) == False
