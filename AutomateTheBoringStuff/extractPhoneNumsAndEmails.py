#! /usr/bin/python3.5

import re, pyperclip

text = pyperclip.paste()

phoneNumbeRegex = re.compile(r'''
                              (\d{3} | \(\d{3}\))?                # 1-optional areacode
                              (\s*|-|\.)?                         # 2-optional separator
                              (\d{3})                             # 3-first three numbers
                              (\s*|-|.)                           # 4-separator
                              (\d{4})                             # 5-last four numbers
                              (\s*,?\s*(ext|x|ext.)\s*(\d{2,5}))? # 6-optional extension
                              ''', re.VERBOSE | re.DOTALL)

phoneMatchObject = phoneNumbeRegex.findall(text)


phoneNumbers = []
for groups in phoneMatchObject:
    phoneNumber = '-'.join([groups[0], groups[2], groups[4]])
    if groups[7] != '':
        phoneNumber += ' ext.' + groups[8]
    phoneNumbers.append(phoneNumber)

print(phoneNumbers)

emailRegex = re.compile(r''' (
                         ([a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]+)  # username
                         (@)                                # at symbol
                         ([a-zA-Z0-9.-]+)                   # domain name
                         (\.[a-zA-Z]{2,4})                  # dot something
                         ) ''', re.VERBOSE | re.IGNORECASE)

emailMatchObject = emailRegex.findall(text)
emails = []
for groups in emailMatchObject:
    emails.append(groups[0])

print(emails)

text = '\n'.join(phoneNumbers) + '\n'
text += '\n'.join(emails)

pyperclip.copy(text)