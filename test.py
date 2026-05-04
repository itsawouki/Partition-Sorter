import json
from sys import intern
from textwrap import indent
resault=[["",""]]
with open('data.json', 'w') as f:
    json.dump(resault, f, indent=2)

print(resault)