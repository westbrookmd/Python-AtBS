#! python3
# searchpypi.py  - Opens several search results.
import requests, sys, webbrowser, bs4

# google solution
search_term = 'python'


print('Googling...')    # display text while downloading the search result page

res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
#res = requests.get('http://google.com/search?q='.format(search_term), 'lxml')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html5lib')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
print ("Link Elements: " + str(linkElems))
print ("Number Open: " + str(numOpen))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))



