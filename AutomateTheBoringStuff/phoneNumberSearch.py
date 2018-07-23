import re

phoneNumberRegex = re.compile(r'(\(\d\d\d\) |\d\d\d-)(\d\d\d-\d\d\d\d)')

matchedObject = phoneNumberRegex.search(
    'my phone number is 617-111-1234 and my friend\'s number is (123) 444-5050.')


areaCode, mainNumber = matchedObject.groups()
print('Area code : ' + matchedObject.group(1))
print('Just numbers : ' + mainNumber)
print('Phone number found: ' + matchedObject.group())


matchedObject = phoneNumberRegex.findall(
    'my phone number is 617-111-1234 and my friend\'s number is (123) 444-5050.')

for group1,group2 in matchedObject:
    print(group1 + group2)