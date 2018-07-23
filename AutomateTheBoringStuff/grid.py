def printRotatedClockwise(list):
    # iterate through the last list
    for column in range(len(list[-1])):
        # iterate with start = lastRow, end = -1, step = -1
        for row in range(len(list) - 1, -1, -1): 
            print(list[row][column], end='')
        print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['O', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

printRotatedClockwise(grid)