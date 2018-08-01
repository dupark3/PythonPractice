#! /usr/bin/python3.5

import bs4, sys, requests, os

url = 'https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)

while not url.endswith('#'):
    print('Downloading page...%s' %(url))
    
    # get response object of main url
    res = requests.get(url)
    res.raise_for_status()
    
    # parse through the html received for a particular element
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    imgElement = soup.select('#comic img')

    if imgElement == []:
        print('Could not find comic at %s' %url)
    else:
        try:
            # create comic url from the src part of the img element
            comicURL = 'https:' + imgElement[0].get('src')
            print('Downloading comic... %s' %(comicURL))
            
            # get a response object from that comic url
            res = requests.get(comicURL)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
            continue

        # create new file and write in byte mode, chunk by chunk
        comicFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            comicFile.write(chunk)
        comicFile.close()

    # back to the original response, find the previous link and get new url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')