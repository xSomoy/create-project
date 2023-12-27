# Version 2.0
# Copyright © Mushphyqur Rahman Tanveer

import sys
import requests as rq
from bs4 import BeautifulSoup as bs


def get_url():      # Get url from user
    # Argument Validation
    if len(sys.argv) < 2:   # IF true no argument has been provided
        # Ask manual input for url and assign to 'url'
        url = ''
        while url == '':
            # Keep asking until url provided
            url = input('Provide Project URL: ')

    else:
        url = sys.argv[1]  # Assign firs argument to 'url'

    return url


def get_beautified_page(url):
    raw = rq.get(url)
    page = bs(raw.text, 'html.parser')
    return page


url = get_url()
page = get_beautified_page(url)

print(page)
