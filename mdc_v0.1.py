import json

# Opening JSON file
with open('data.json', 'r') as openfile:

    # Reading from json file
    data = json.load(openfile)

# Skills formating


def skills_format(sk=data['skills']):  # demo : **C# Programming** |
    skills = ''
    for i in sk:
        i = '**' + i + '**' + " | "
        skills = skills + i
    skills = skills[:-2]
    return skills


skills = skills_format(data['skills'])


markdown_content = f'''
# [{data['title1']}]({data['url']})
## Project ID: {data['platform']}
> Price : **{data['price'].lstrip()}**

> Status : {data['status']}

> Entry Recieved : {data['entry']}

## Description:
```
{data['description']}

```
---
## Supported Submission File Types:

> TYPE, TYPE

## Recommended Skills:


{skills}

---
***Comments***
- 
'''

file_path = 'Project-Info.md'

with open(file_path, 'w') as file:
    file.write(markdown_content)
