#! /usr/bin/python3.5

import webbrowser, bs4, requests, sys


# get keywords from sys.argv
if len(sys.argv) < 2:
    print('Must enter keywords to google search.')
    sys.exit()
else:
    keywords = ' '.join(sys.argv[1:])

# download html from google.com/keywords
res = requests.get('https://google.com/search?q=%s' %(keywords))
res.raise_for_status()


# use beautiful soup to parse and find the first 5 links if any
soup = bs4.BeautifulSoup(res.text, 'lxml')
elements = soup.select('.r > a')

# open those links with webbrowser.open() if any
for i in range(min(5, len(elements))):
    webbrowser.open('https://google.com' + elements[i].get('href'))

