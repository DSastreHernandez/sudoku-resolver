def check_rows_in_sudoku(sudoku):
    for row in sudoku:
        for number in row:
            if not row.count(number) == 1:
                return False
    return True

#parte del código que no se va a ejecutar
if __name__ == '__main__':
    assert check_rows_in_sudoku([[1, 2, 3],
                                 [2, 3, 1],
                                 [3, 1, 2]]) == True
    assert check_rows_in_sudoku([[1, 2, 3, 4],
                                 [2, 3, 1, 3],
                                 [3, 1, 2, 3],
                                 [4, 4, 4, 4]]) == False
    assert check_rows_in_sudoku([[1, 2, 3, 4],
                                 [2, 3, 1, 4],
                                 [4, 1, 2, 3],
                                 [3, 4, 1, 2]]) == True
    assert check_rows_in_sudoku([[1, 2, 3, 4, 5],
                                 [2, 3, 1, 5, 6],
                                 [4, 5, 2, 1, 3],
                                 [3, 4, 5, 2, 1],
                                 [5, 6, 4, 3, 2]]) == True
    assert check_rows_in_sudoku([[1, 2, 3, 4, 5],
                                 [2, 3, 1, 5, 6],
                                 [4, 5, 2, 1, 3],
                                 [3, 4, 5, 2, 1],
                                 [5, 6, 4, 3, 2]]) == True
    assert check_rows_in_sudoku([['a', 'b', 'c'],
                                 ['b', 'c', 'a'],
                                 ['c', 'a', 'b']]) == True
    assert check_rows_in_sudoku([[1, 1.5],
                                 [1.5, 1]]) == True
    assert check_rows_in_sudoku([[1, 0, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 0, 1]]) == False
