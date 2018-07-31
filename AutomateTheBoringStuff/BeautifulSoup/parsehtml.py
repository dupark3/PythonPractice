#! /usr/bin/python3.5

import bs4, requests

res = requests.get('http://nostarch.com/')
try:
    res.raise_for_status()
except Exception as exc:
    print('HTTP Request exception raised: %s' %(exc))

fileobj = open('sample.html','r')
soup = bs4.BeautifulSoup(fileobj, 'lxml')

elements = soup.select('#author')
# elements is a list of Tag objects

# tag objects have .text method to return the string
print(elements[0].getText())

# tag objects have .attrs method which returns a dictionary of attributes with value
print(elements[0].attrs)

elements = soup.select('p')

for i in range(len(elements)):
    print(elements[i].text)