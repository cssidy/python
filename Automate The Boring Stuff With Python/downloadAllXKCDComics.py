#! python3
# downloads every single XKCD comic

import requests, os, bs4

# starting url
url = 'http://xkcd.com'

# stores comics in ./xkcd
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # find the url of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find a comic image.')

    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # TODO: save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # TODO: get the prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')

