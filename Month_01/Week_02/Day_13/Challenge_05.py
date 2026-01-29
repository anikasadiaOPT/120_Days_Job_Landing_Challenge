# JSON Serialization

import json
data = {
    "Name": "Alina",
    "ID": "124",
    "Age": 40
}

try:
    with open("data.json", "w") as file:
        json.dump(data, file)
except FileNotFoundError as e:
    print("The file is not found..")




# Output:
"""
{"Name": "Alina", "ID": "124", "Age": 40}
"""