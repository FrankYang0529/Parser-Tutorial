import requests
import bs4

distros = ['http://www.bbc.com/news/election-us-2016-35760148', 'http://www.bbc.com/news/world-europe-35760985', 'http://www.bbc.com/news/world-asia-35760797']

for distro in distros:
    page = requests.get(distro)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    print (distro, soup.title)
