import bs4
import asyncio
import aiohttp

@asyncio.coroutine
def get(*args, **kwargs):
    response = yield from aiohttp.request('GET', *args, **kwargs)
    return (yield from response.read())

def first_magnet(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    return soup.title

@asyncio.coroutine
def print_magnet(query):
    url = query
    page = yield from get(url, compress=True)
    magnet = first_magnet(page)
    print('{}: {}'.format(query, magnet))

distros = ['http://www.bbc.com/news/election-us-2016-35760148', 'http://www.bbc.com/news/world-europe-35760985', 'http://www.bbc.com/news/world-asia-35760797']
loop = asyncio.get_event_loop()
f = asyncio.wait([print_magnet(d) for d in distros])
loop.run_until_complete(f)
