import sys
import os
from datetime import datetime as dt

# Argument Validation
if len(sys.argv) < 2:
    print('No Argument is provided!')
    exit()

# Project folder creation
year = dt.now().year % 1000
month = dt.now().month

# EX: FR C 02 WebScrap
platform = sys.argv[1]
project_type = sys.argv[2]
id = sys.argv[3]
project_name = sys.argv[4]


os.mkdir(f'{platform}{year}{month}P{project_type}{id}-{project_name}')


# Project Info Creator
project_url = input('Project URL: ')
markdown_content = f'''
# [{project_name}]({project_url})
## Project ID: {platform}{year}{month}P{project_type}{id}
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

project_folder = f'{platform}{year}{month}P{project_type}{id}-{project_name}'
os.chdir(project_folder)

file_path = 'Project-Info.md'

with open(file_path, 'w') as file:
    file.write(markdown_content)
