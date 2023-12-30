# Version 2.0
# Copyright © Mushphyqur Rahman Tanveer

import os
import sys
import json
import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
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

    no = no.zfill(2)

    return no, url

# Download the page and beutify it


def get_beautified_page(url):
    raw = rq.get(url)
    page = bs(raw.text, 'html.parser')
    print('Process(1/69): Project Page Downloaded!')
    return page


# Get platform and project type from url
def get_platform_and_type(url):
    if 'freelancer' in url:
        platform = 'Freelancer'
    else:
        platform = 'UNKOWN'
    print('Process(2/69): Platform Detected!')
    if 'contest' in url:
        project_type = 'Contest'
    else:
        project_type = 'Unkown'
    print('Process(3/69): Project Type Detected!')
    return platform, project_type


# Get Project Title
def get_project_title(url, page):
    directory_title = '_'.join(url.split('/')[4].split('-')[:-1])
    md_title = page.title.text.split('|')[0]
    print('Process(4/69): Project Title Generated!')
    return directory_title, md_title


# Get project description
def get_project_description(page):
    description = page.p.text
    print('Process(5/69): Project Description Extracted!')
    return description


# Get recommed skills
def get_skills(page):
    skills = []
    temp_skills = page.find_all('ul')[3].find_all('a')
    for i in temp_skills:
        skills.append(i.text)
    print('Process(6/69): Project Required Skills Collected!')
    return skills


# Get Status Price And Entry Recived
def get_staus_price_entry(page):
    status_price_entry = []
    temp = page.find_all('ul')[2].find_all('li')
    for i in temp:
        status_price_entry.append(i.text.strip().split(':')[1].lstrip())
    print('Process(7/69): Project Status, Price and Total Enties Collected!')
    return status_price_entry


# Project ID creator EX. FR2312C01
def project_id_creator(no, platform, project_type):
    year = dt.now().year % 1000
    month = dt.now().month
    match platform:
        case 'Freelancer':
            platform = 'FR'
        case 'Fiverr':
            platform = 'FI'
        case _:
            platform = platform
    match project_type:
        case 'Contest':
            project_type = 'C'
        case 'Project':
            project_type = 'P'
        case _:
            project_type = project_type
    date = dt.now().date()
    ID = platform + str(year) + str(month) + project_type + no
    print('Process(8/69): Project ID Generated!')
    return ID, str(date)

# JSON file creator


def make_json(date, no, ID, url, platform, project_type, directory_title, md_title, status, price, entry, skills, description):
    data = {
        'date': date,
        'no': no,
        'id': ID,
        'url': url,
        'platform': platform,
        'type': project_type,
        'title0': directory_title,
        'title1': md_title,
        'status': status,
        'price':  price,
        'entry': entry,
        'skills': skills,
        'description': description
    }
    # Serializing json
    json_object = json.dumps(data, indent=4)
    print('Process(8/69): JSON Object Created!')
    # Writing to sample.json
    with open(f'{ID}.json', 'w') as outfile:
        outfile.write(json_object)
    print('Process(10/69): Project JSON Data Stored!')


# Processing Informations
no, url = get_url_no()
page = get_beautified_page(url)
platform, project_type = get_platform_and_type(url)
directory_title, md_title = get_project_title(url, page)
status, price, entry = get_staus_price_entry(page)
skills = get_skills(page)
description = get_project_description(page)
ID, date = project_id_creator(no, platform, project_type)


# ----------------------------Project Enviroment Creation---------------------------------------


# Skills formating for makrdown systax


def skills_format(sk=skills):  # demo : **C# Programming** |
    skills = ''
    for i in sk:
        i = '**' + i + '**' + " | "
        skills = skills + i
    skills = skills[:-2]
    return skills


skills = skills_format(skills)


# Creating Project directory

project_directory = f'{ID}-{directory_title}'
os.mkdir(project_directory)
print('Process(11/69): Project Directory Created!')
os.chdir(project_directory)
print('Process(12/69): Changing Working Directory to Project Directory!')


# Generating Project-info.md

# Project Markdown Content
project_info_md = f'''
# [{md_title}]({url})
## Project ID: {ID}
> Price : **{price}**

> Status : {status}

> Entry Recieved : {entry}

## Description:
```
{description}

```
---

## Recommended Skills:

{skills}


## Supported Submission File Types:

> TYPE, TYPE 
'''
print('Process(13/69): Project_Info.md Generated!')

# writing Project.md File
file_path = 'Project_Info.md'
with open(file_path, 'w') as file:
    file.write(project_info_md)

print('Process(14/69): Project_Info.md Created!')

# Generating Entry_Info Markdown Created
entry_info_md = f'''
***ENTRY TITLE***
> 

***Describe your entry***

ENTRY DESCRIPTION

'''

# Craeting the Entry-Info Markdown file
print('Process(15/69): Entry_Info.md Generated!')
file_path = 'Entry_Info.md'
with open(file_path, 'w') as file:
    file.write(entry_info_md)
print('Process(16/69): Entry_Info.md Created!')

# END

# ----------------------------- JSON FILE GENERATOR ------------------

make_json(date, no, ID, url, platform, project_type, directory_title, md_title,
          status, price, entry, skills, description)

print('PROJECT ENVIROMENT IS READY!!!!')
