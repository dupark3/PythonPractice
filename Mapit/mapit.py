#! /usr/bin/python3.5

import webbrowser, pyperclip, sys, logging
# logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -- %(levelname)s -- %(message)s')

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

logging.debug('Address is %s' %(address))

address = 'https://www.google.com/maps/place/' + address
webbrowser.open(address)