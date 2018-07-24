#! /usr/bin/python3.5

# A strong password is one that is at least 8 chars long
# At least one upper case letter, at least one lowercase letter
# At least one number

import re, sys

if len(sys.argv) < 2:
    print('Usage: ./strongPasswordDetection.py \"password\"')
    sys.exit()

password = sys.argv[1]
weak = False

if len(password) < 8:
    print('Must be longer than 8 characters')
    weak = True

upperCaseRegex = re.compile(r'[A-Z]+')
lowerCaseRegex = re.compile(r'[a-z]+')
numberRegex    = re.compile(r'\d+')

upperMatchObject = upperCaseRegex.search(password)
lowerMatchObject = lowerCaseRegex.search(password)
numberMatchObject= numberRegex.search(password)

if upperMatchObject  == None:
    print('Must have at least one upper case letter')
    weak = True
if lowerMatchObject  == None:
    print('Must have at least one lower case letter')
    weak = True
if numberMatchObject == None:    
    print('Must have at least one digit')
    weak = True

if weak is False:
    print('Strong password')
