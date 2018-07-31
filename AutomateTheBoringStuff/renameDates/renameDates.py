#! /usr/bin/python3.5

import re, os, shutil

# create american data regex MM-DD-YYYY or M-D-YY
americanDate = re.compile(r'''
                           ^(.*?)            # 1 - prefix
                           ([0,1]?\d-)       # 2 - months, one or two digits
                           ([0,1,2,3]?\d-)   # 3 - days, one or two digits
                           (\d{2,4})         # 4 - year, two to four digits
                           (.*?)$            # 5 - suffix
                           ''', re.VERBOSE)



# walk through all files
currentDir = os.getcwd()
print('current dir: ' + currentDir)
for current, subfolders, subfiles in os.walk(currentDir):
    print(current)
    for folder in subfolders:
        print('    folder in current: ' + folder)
    for file in subfiles:
        print('    file in current: ' + file)
        flieMatchObj = americanDate.search(file)
        if flieMatchObj:
            fileMatchGroups = flieMatchObj.groups()
            newName = fileMatchGroups[0] + fileMatchGroups[2] + fileMatchGroups[1] + fileMatchGroups[3] + fileMatchGroups[4]
            print('        ' + newName)
            shutil.move(os.path.join(current,file), os.path.join(current, newName))
