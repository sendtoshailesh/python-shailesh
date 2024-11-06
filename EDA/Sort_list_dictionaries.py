dict1 = [
    {"Name":"Karl",
     "Age":25},
     {"Name":"Lary",
     "Age":39},
     {"Name":"Nina",
     "Age":35}
]

## Using sort()
dict1.sort(key=lambda item: item.get("Age"))

# List sorting using itemgetter
from operator import itemgetter
f = itemgetter('Name')
dict1.sort(key=f)

# Iterable sorted function
dict1 = sorted(dict1, key=lambda item: item.get("Age"))

'''Output
[{'Age': 25, 'Name': 'Karl'},
 {'Age': 35, 'Name': 'Nina'},
 {'Age': 39, 'Name': 'Lary'}]
'''
