# Version 2.0
# Copyright © Mushphyqur Rahman Tanveer

import sys
import requests as rq
from bs4 import BeautifulSoup as bs


# Get url from user
def get_url():
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


# Download the page and beutify it
def get_beautified_page(url):
    raw = rq.get(url)
    page = bs(raw.text, 'html.parser')
    return page


# Get platform and project type from url
def get_platform_and_type(url):
    if 'freelancer' in url:
        platform = 'Freelancer'
    else:
        platform = 'UNKOWN'
    if 'contest' in url:
        type = 'Contest'
    else:
        type = 'Unkown'
    return platform, type


# Main Processing
url = get_url()
page = get_beautified_page(url)
plaform = get_platform_and_type(url)[0]
type = get_platform_and_type(url)[1]

print(plaform)
print(type)
