# Version 2.0
# Copyright © Mushphyqur Rahman Tanveer

import sys
import json
import requests as rq
from bs4 import BeautifulSoup as bs

# Get url and ID from user


def get_url_no():
    # Argument Validation
    if len(sys.argv) < 2:   # IF true no argument has been provided
        # Ask manual input for url and project number then assign to 'url' and 'No'
        no = input('Provide Project No. ')
        url = input('Provide Project URL: ')

    elif len(sys.argv) < 3:
        if sys.argv[1].isdigit():
            no = sys.argv[1]
            url = input('Provide Project URL: ')
        else:
            url = sys.argv[1]
            no = input('Provide Project No. ')

    else:
        no = sys.argv[1]  # Assign Fist argument to 'no'
        url = sys.argv[2]  # Assign Second argument to 'url'

    return no, url

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

def make_json(no, url, plaform, project_type, folder_title, md_title, status, price, entry, skills, description):
    data = {
        'no': no,
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
no, url = get_url_no()
page = get_beautified_page(url)

# Fetched Informations
plaform, project_type = get_platform_and_type(url)
folder_title, md_title = get_project_title(url, page)
status, price, entry = get_staus_price_entry(page)
skills = get_skills(page)
description = get_project_description(page)


make_json(no, url, plaform, project_type, folder_title, md_title,
          status, price, entry, skills, description)
