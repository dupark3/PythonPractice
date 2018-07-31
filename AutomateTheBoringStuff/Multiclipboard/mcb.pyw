#! /usr/bin/python3.5

import pyperclip, sys, shelve, pprint

# ./mcb.pyw list
# ./mcb.pyw save <keyword>
# ./mcb.pyw <keyword>
# ./mcb.pyw delete <keyword>
# ./mcb.pyw delete_all

mcbShelf = shelve.open('clipboard')

if len(sys.argv) < 2:
    print('Usage error. Try typing save, list, or a keyword')

# Load all keys into the clipboard
elif sys.argv[1].lower() == 'list':
    pyperclip.copy(pprint.pformat(list(mcbShelf.keys())) )

# Save current clipboard into keyword
elif sys.argv[1].lower() == 'save' and len(sys.argv) == 3:
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    
# Delete a specific key
elif sys.argv[1].lower() == 'delete' and len(sys.argv) == 3:
    del mcbShelf[sys.argv[2]]

# Delete all keys
elif sys.argv[1].lower() == 'delete_all':
    for key in list(mcbShelf.keys()):
        del mcbShelf[key]

# Accesing a keyword, obtain clipped text of this keyword if it exists
else: 
    if sys.argv[1] in list(mcbShelf.keys()):
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print(sys.argv[1] + ' is not a valid key.')

mcbShelf.close()