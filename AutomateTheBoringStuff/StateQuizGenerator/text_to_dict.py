fileObj = open('state_capitals.txt', 'r')
capitals = open('state_capitals.py', 'w')

capitals.write('capitals = [ ')

for line in fileObj:
    lists = line.split('    ')
    capitals.write('{ \'' + lists[0] + '\':\'' + lists[1] + '\'},\n')

capitals.write(']')