# Version 2.0
# Copyright © Mushphyqur Rahman Tanveer

import sys
import json
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


# Get project description
def get_project_description(page):
    description = page.p.text
    return description


# Get recommed skills
def get_skills(page):
    skills = []
    temp_skills = page.find_all('ul')[3].find_all('a')
    for i in temp_skills:
        skills.append(i.text)
    return skills


# Get Status Price And Entry Recived
def get_staus_price_entry(page):
    status_price_entry = []
    temp = page.find_all('ul')[2].find_all('li')
    for i in temp:
        status_price_entry.append(i.text.strip().split(':')[1])
    return status_price_entry


# JSON file creator

def make_json(url, plaform, project_type, folder_title, md_title, status, price, entry, skills, description):
    data = {
        'url': url,
        'platform': plaform,
        'type': project_type,
        'title0': folder_title,
        'title1': md_title,
        'status': status,
        'price':  price,
        'entry': entry,
        'skills': skills,
        'description': description
    }
    # Serializing json
    json_object = json.dumps(data, indent=4)

    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)


# Main Processing
url = get_url()
page = get_beautified_page(url)

# Fetched Informations
plaform = get_platform_and_type(url)[0]
project_type = get_platform_and_type(url)[1]
folder_title = get_project_title(url, page)[0]
md_title = get_project_title(url, page)[1]
status = get_staus_price_entry(page)[0]
price = get_staus_price_entry(page)[1]
entry = get_staus_price_entry(page)[2]
skills = get_skills(page)
description = get_project_description(page)


make_json(url, plaform, project_type, folder_title, md_title,
          status, price, entry, skills, description)

# print(plaform, project_type, folder_title,
#       md_title, skills, status, price, entry)
# print(description)
