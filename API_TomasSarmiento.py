import requests
import json
import ast
import pandas as pd
from pandas.io.json import json_normalize
# response = request.get("https://pokeapi.co/api/v2/ability/7/")
response = requests.get("https://pokeapi.co/api/v2/pokemon-form/132/")

print('ORIGINAL DATA: ...................................................')
print(response.status_code)
print(response.json())


def jsonFn(obj):
    text = json.dumps(obj, sort_keys=True, indent=2)
    return text

print('Json DATA: ...................................................')
data = jsonFn(response.json())
print(data)










