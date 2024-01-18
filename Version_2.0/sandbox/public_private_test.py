
from bs4 import BeautifulSoup as bs
import requests as rq

url = 'https://www.freelancer.com/contest/2356838' # Private
# url = 'https://www.freelancer.com/contest/lichess-full-installation-2357414' # Public
raw = rq.get(url)
page = bs(raw.text, 'html.parser')
if 'Login' in page.title.text:
    print('the contest is private')
else:
    print('ok')
