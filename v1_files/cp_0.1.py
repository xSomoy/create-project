import sys
import os
from datetime import datetime as dt

if len(sys.argv) < 2:
    print('No Argument is provided!')
    exit()

year = dt.now().year % 1000
month = dt.now().month
platform = sys.argv[1]
id = sys.argv[2]
project_name = sys.argv[3]


os.mkdir(f'{platform}{year}{month}C{id}-{project_name}')
