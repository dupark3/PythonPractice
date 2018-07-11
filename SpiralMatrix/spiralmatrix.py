def spiralprint(matrix):
    height = len(matrix)
    width = len(matrix[0])
    rowsPrinted = [-1, height]
    columnsPrinted = [-1, width]
    i = j = 0
    total = height * width
    count = 0
    up = down = left = False
    right = True
    while (count != total):
        #print("i : ", i, " j : ", j)
        count += 1
        print(matrix[i][j], end=" ")
        if right:
            if j + 1 in columnsPrinted:
                right = False
                down = True
                rowsPrinted.append(i)
                i += 1
                continue
            else:
                j += 1
        if down:
            if i + 1 in rowsPrinted:
                down = False
                left = True
                columnsPrinted.append(j)
                j -= 1
                continue
            else:
                i += 1
        if left:
            if j - 1 in columnsPrinted:
                left = False
                up = True
                rowsPrinted.append(i)
                i -= 1
                continue
            else:
                j -= 1
        if up:
            if i - 1 in rowsPrinted:
                up = False
                right = True
                columnsPrinted.append(j)
                j += 1
                continue
            else:
                i -= 1


    print()

matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

spiralprint(matrix)