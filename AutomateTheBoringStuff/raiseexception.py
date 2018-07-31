#! /usr/bin/python3.5

def drawBox(char, width, height):
    if len(char) != 1:
        raise Exception('Symbol must be one character for the box border.')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')

    # top of the box
    print(char * width)

    # middle of the box
    for i in range(height-2):
        print(char + ' ' * (width - 2) + char)

    # bottom of the box
    print(char * width)
    

for char, width, height in [ ['*', 3, 5], ['O', 10, 5], ['1', 5, 2], ['**', 4, 4] ]:
    try:
        drawBox(char, width, height)
    except Exception as err:
        print(err)
