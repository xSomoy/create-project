# Version 1.0
# Copyright © Mushphyqur Rahman Tanveer

import sys
import os
from datetime import datetime as dt

# Argument Validation
if len(sys.argv) < 2:
    print('No Argument is provided!')
    print('Argument Fortmat: Platfrom Project Type No Name')
    print('EX: FR C 02 WebScrap')
    exit()

# Project folder creation
year = dt.now().year % 1000
month = dt.now().month

# Getting All Info
# EX: FR C 02 WebScrap
platform = sys.argv[1]
project_type = sys.argv[2]
id = sys.argv[3]
project_name = sys.argv[4]

# Displaying Information Collected
print(f'Platform: {platform}\nType: {project_type}\nProject ID: {platform}{year}{month}{project_type}{id}\nProject Name: {project_name}')

# Collecting Project URL
project_url = input('Project URL: ')

# Creating Project Folder
os.mkdir(f'{platform}{year}{month}{project_type}{id}-{project_name}')
print('Project Folder Created')
# Project Info Creator
markdown_content = f'''
# [{project_name}]({project_url})
## Project ID: {platform}{year}{month}{project_type}{id}
## Description:
```
DESCRIPTION

```
---
## Supported Submission File Types:

> TYPE, TYPE

## Recommended Skills:


**SKILL** | **SKILL**  

---
***Comments***
- 
'''
# Changinf directory
project_folder = f'{platform}{year}{month}{project_type}{id}-{project_name}'
os.chdir(project_folder)
print('Changing Directory')

# Craeting the Project-Info Markdown file
file_path = 'Project-Info.md'
with open(file_path, 'w') as file:
    file.write(markdown_content)
print('Project Info Markdown Created!')

# Created Entry Info Markdown Created
markdown_content = f'''
***ENTRY TITLE***
> 

***Describe your entry***

ENTRY DESCRIPTION

'''

# Craeting the Project-Info Markdown file
file_path = 'Entry-Info.md'
with open(file_path, 'w') as file:
    file.write(markdown_content)
print('Entry Info Markdown Created!')

# END
