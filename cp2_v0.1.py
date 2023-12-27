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
        project_type = 'Contest'
    else:
        project_type = 'Unkown'
    return platform, project_type

# Get Project Title


def get_project_title(url, page):
    folder_title = '_'.join(url.split('/')[4].split('-')[:-1])
    md_title = page.title.text.split('|')[0]
    return folder_title, md_title


# Main Processing
url = get_url()
page = get_beautified_page(url)

# Fetched Informations
plaform = get_platform_and_type(url)[0]
project_type = get_platform_and_type(url)[1]
folder_title = get_project_title(url, page)[0]
md_title = get_project_title(url, page)[1]

print(plaform, project_type, folder_title, md_title)
