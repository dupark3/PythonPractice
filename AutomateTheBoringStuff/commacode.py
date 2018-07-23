
def commaSeparate(list):
    if len(list) == 0:
        return ''

    returnString = str(list[0])
    for i in range(1,len(list)):
        returnString += ', '
        if i == len(list) - 1:
            returnString += 'and '
        returnString += str(list[i])
        
    return returnString
        

spam = ['cat', 'dog', 'mouse']
spam =[1, 3, 5, 'dog', 3.55, [1, 5]]
print(commaSeparate(spam))
