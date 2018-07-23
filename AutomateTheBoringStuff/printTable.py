#! /usr/bin/python3.5

def printTable(table):
    """ prints table with every item aligned to the right """
    maxLengths = []
    for column in range(len(table[0])):
        maxLen = 0
        for row in range(len(table)):
            if len(table[row][column]) > maxLen:
                maxLen = len(table[row][column])
        maxLengths.append(maxLen)

    for row in range(len(table)):
        for column in range(len(table[row])):
            print(table[row][column].rjust(maxLengths[column]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bobbbymcbobber', 'Carol', 'David'],
             ['dogs', 'cats', 'mooseeseee', 'goose']]

printTable(tableData)

"""

apples oranges cherries banana
 Alice     Bob    Carol  David
  dogs    cats    moose  goose

"""