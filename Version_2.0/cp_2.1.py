# Version 2.0
# Copyright © Mushphyqur Rahman Tanveer

import os
import sys
import json
import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt

tp = 16  # Total Processes

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
    if 'Login' in page.title.text:
        print('PRIVATE CONTEST DETECTED!!\nProcress Terminated!')
        exit()
    print(f'Process(1/{tp}): Project Page Downloaded!')
    return page


# Get platform and project type from url
def get_platform_and_type(url):
    if 'freelancer' in url:
        platform = 'Freelancer'
    else:
        platform = 'UNKOWN'
    print(f'Process(2/{tp}): Platform Detected!')
    if 'contest' in url:
        project_type = 'Contest'
    else:
        project_type = 'Unkown'
    print(f'Process(3/{tp}): Project Type Detected!')
    return platform, project_type


# Get Project Title
def get_project_title(url, page):
    directory_title = '_'.join(url.split('/')[4].split('-')[:-1])
    md_title = page.title.text.split('|')[0]
    print(f'Process(4/{tp}): Project Title Generated!')
    return directory_title, md_title


# Get project description
def get_project_description(page):
    description = page.p.text
    print(f'Process(7/{tp}): Project Description Extracted!')
    return description


# Get recommed skills
def get_skills(page):
    skills = []
    temp_skills = page.find_all('ul')[3].find_all('a')
    for i in temp_skills:
        skills.append(i.text)
    print(f'Process(6/{tp}): Project Required Skills Collected!')
    return skills


# Get Status Price And Entry Recived
def get_staus_price_entry(page):
    status_price_entry = []
    temp = page.find_all('ul')[2].find_all('li')
    for i in temp:
        status_price_entry.append(i.text.strip().split(':')[1].lstrip())
    print(
        f'Process(5/{tp}): Project Status, Price and Total Enties Collected!')
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
    print(f'Process(8/{tp}): Project ID Generated!')
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
    print(f'Process(15/{tp}): JSON Object Created!')
    # Writing to sample.json
    with open(f'{ID}.json', 'w') as outfile:
        outfile.write(json_object)
    print(f'Process(16/{tp}): Project JSON Data Stored!')


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
print(f'Process(9/{tp}): Project Directory Created!')
os.chdir(project_directory)
print(f'Process(10/{tp}): Changing Working Directory to Project Directory!')


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
print(f'Process(11/{tp}): Project_Info.md Generated!')

# writing Project.md File
file_path = 'Project_Info.md'
with open(file_path, 'w') as file:
    file.write(project_info_md)

print(f'Process(12/{tp}): Project_Info.md Created!')

# Generating Entry_Info Markdown Created
entry_info_md = f'''
***ENTRY TITLE***
> 

***Describe your entry***

ENTRY DESCRIPTION

'''

# Craeting the Entry-Info Markdown file
print(f'Process(13/{tp}): Entry_Info.md Generated!')
file_path = 'Entry_Info.md'
with open(file_path, 'w') as file:
    file.write(entry_info_md)
print(f'Process(14/{tp}): Entry_Info.md Created!')

# END

# ----------------------------- CREATING JSON FILE ------------------

make_json(date, no, ID, url, platform, project_type, directory_title, md_title,
          status, price, entry, skills, description)


# ---------------------- DISPLAYING ALL INFORMATIONS ------------------
print('\n--------------------------------------------------------\n')
print(f'Project No. {no}\nID: {ID}\nProject Name: {md_title}\nProject Directory: {project_directory}\nInfo: {project_directory}/Project_info.md\nProject Data: {project_directory}/{ID}.json\nEntry Template:{project_directory}/Entry_Info.md\nProject URL: {url}\nPlatform: {platform}\nProject Type: {project_type}\nStatus: {status}\nPrice: {price}')
print('\nPROJECT ENVIROMENT IS READY!!!!')


######################## -------- DONE ----------##########################
