def check_columns_in_sudoku(sudoku):
    turns = 0
    counter = len(sudoku)
    while counter > 0:
        column = []
        for element in sudoku:
            column.append(element[turns])
        for number in column:
            if not column.count(number) == 1:
                return False
        turns += 1
        counter -= 1
    return True


if __name__ == '__main__':
    assert check_columns_in_sudoku([[1, 2, 3],
                                    [2, 3, 1],
                                    [3, 1, 2]]) == True
    assert check_columns_in_sudoku([[1, 2, 3, 4],
                                    [2, 3, 1, 3],
                                    [3, 1, 2, 3],
                                    [4, 4, 4, 4]]) == False
    assert check_columns_in_sudoku([[1, 2, 3, 4],
                                    [2, 3, 1, 4],
                                    [4, 1, 2, 3],
                                    [3, 4, 1, 2]]) == False
    assert check_columns_in_sudoku([[1, 2, 3, 4, 5],
                                    [2, 3, 1, 5, 6],
                                    [4, 5, 2, 1, 3],
                                    [3, 4, 5, 2, 1],
                                    [5, 6, 4, 3, 2]]) == True
    assert check_columns_in_sudoku([[1, 2, 3, 4, 5],
                                    [2, 3, 1, 5, 6],
                                    [4, 5, 2, 1, 3],
                                    [3, 4, 5, 2, 1],
                                    [5, 6, 4, 3, 2]]) == True
    assert check_columns_in_sudoku([['a', 'b', 'c'],
                                    ['b', 'c', 'a'],
                                    ['c', 'a', 'b']]) == True
    assert check_columns_in_sudoku([[1, 1.5],
                                    [1.5, 1]]) == True
    assert check_columns_in_sudoku([[1, 0, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 0, 1]]) == False
