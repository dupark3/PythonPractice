#! /usr/bin/python3.5

# regex version of string.strip() which removes whitespace
# if a second argument is provided, strip those chars

import re

def regexStrip(text, strip=r'\s'):
    stripLeadingRegexObject = re.compile(r'^[%s]+'%strip)
    stripTrailingRegexObject = re.compile(r'[%s]+$'%strip)
    matchObject = stripLeadingRegexObject.sub('', text)
    matchObject = stripTrailingRegexObject.sub('', str(matchObject))
    
    return str(matchObject)

# end showing \n raw string to show that trailing whitespace is stripped
print(regexStrip('  Hello  '), end=r'\n''\n') 
print(regexStrip('spamspambacoiseggspam', 'apms'))