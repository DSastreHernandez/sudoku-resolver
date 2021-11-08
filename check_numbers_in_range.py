def check_numbers_in_range(sudoku):
    rango_sudoku = len(sudoku) + 1
    for element in sudoku:
        for number in element:
            if not number in range(1, rango_sudoku):
                return False
    return True


if __name__ == '__main__':
    assert check_numbers_in_range([[1, 2, 3],
                                   [2, 3, 1],
                                   [3, 1, 2]]) == True
    assert check_numbers_in_range([[1, 2, 3, 4],
                                   [2, 3, 1, 3],
                                   [3, 1, 2, 3],
                                   [4, 4, 4, 4]]) == True
    assert check_numbers_in_range([[1, 2, 3, 4],
                                   [2, 3, 1, 4],
                                   [4, 1, 2, 3],
                                   [3, 4, 1, 2]]) == True
    assert check_numbers_in_range([[1, 2, 3, 4, 5],
                                   [2, 3, 1, 5, 6],
                                   [4, 5, 2, 1, 3],
                                   [3, 4, 5, 2, 1],
                                   [5, 6, 4, 3, 2]]) == False
    assert check_numbers_in_range([[1, 2, 3, 4, 5],
                                   [2, 3, 1, 5, 6],
                                   [4, 5, 2, 1, 3],
                                   [3, 4, 5, 2, 1],
                                   [5, 6, 4, 3, 2]]) == False
    assert check_numbers_in_range([['a', 'b', 'c'],
                                   ['b', 'c', 'a'],
                                   ['c', 'a', 'b']]) == False
    assert check_numbers_in_range([[1, 1.5],
                                   [1.5, 1]]) == False
    assert check_numbers_in_range([[1, 0, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 0, 1]]) == False
