def spiralprint(matrix):
    """
    spiralprint takes a 2D matrix as input and prints 
    all elements in spiral form, going right, down, left, and up. 
    """

    # initialize rowsPrinted and columnsPrinted with the edges
    rowsPrinted = [-1, len(matrix)]
    columnsPrinted = [-1, len(matrix[0])]

    # integer values used to index the matrix and move through the while loop
    row = column = 0
    totalElements = len(matrix) * len(matrix[0])
    totalPrinted = 0

    # four flags, right is True to start since we go to the right first.
    up = down = left = False
    right = True
    
    # loop prints one element each time. checks for the correct directional flag.
    while (totalPrinted < totalElements):
        print(matrix[row][column], end=" ")
        totalPrinted += 1

        if right:
            if column + 1 in columnsPrinted:
                right = False
                down = True
                rowsPrinted.append(row)
                row += 1
                continue
            else:
                column += 1
        if down:
            if row + 1 in rowsPrinted:
                down = False
                left = True
                columnsPrinted.append(column)
                column -= 1
                continue
            else:
                row += 1
        if left:
            if column - 1 in columnsPrinted:
                left = False
                up = True
                rowsPrinted.append(row)
                row -= 1
                continue
            else:
                column -= 1
        if up:
            if row - 1 in rowsPrinted:
                up = False
                right = True
                columnsPrinted.append(column)
                column += 1
                continue
            else:
                row -= 1
    print() # print a newline after while loop is done

matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [ [1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

spiralprint(matrix)
spiralprint(matrix2)