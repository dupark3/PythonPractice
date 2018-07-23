#! /usr/bin/python3.5
# An insecure password manager program

import sys
import pyperclip
from werkzeug.security import check_password_hash, generate_password_hash

passwords = {
             'email' : 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog' : 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage' : '12345'
            }

masterPasswordHash = generate_password_hash('admin')

if len(sys.argv) < 3:
    print('Usage: ./passwordmanager.py {master password} {account name}')
    sys.exit()

if check_password_hash(masterPasswordHash, sys.argv[1]) is False:
    print('Incorrect master password, exiting program')
    sys.exit()

account = sys.argv[2] # second command line argument should be the account name


if account in passwords:
    pyperclip.copy(passwords[account])
    print(account + ' password copied to your clipboard.')
else:
    print(account + ' does not exist in this manager. If you would like to store a password for ' 
          + account + ', enter it now: ')
    newPassword = input()
    passwords[account] = newPassword
    print('Password for ' + account + ' set.')

