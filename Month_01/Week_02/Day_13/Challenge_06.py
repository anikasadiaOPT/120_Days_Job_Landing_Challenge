# CSV Parsing 

import csv
data = [
    {"Name": "Anika", "Age": 34, "ID": 234},
    {"Name": "Anima", "Age": 45, "ID": 561}
]

try:
    with open("output.csv", "w", encoding = "utf-8", newline = "") as file:
        fieldnames = ["Name", "Age", "ID"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)

        writer.writeheader()

        writer.writerows(data)

        print("The list of Dictionaries have read..")
except Exception as e:
    print(f"The error: {e}")




# Output:

"""
The list of Dictionaries have read..
"""



# Read the list of Dictionaries
try:
    with open("output.csv", "r", encoding = "utf-8") as new_file:
        reader = csv.DictReader(new_file)
        for row in reader:
            print(f"{row['Name']} is {row['Age']}, her ID is {row['ID']}")
        print("The file is read..")
except Exception as e:
    print(f"The Error:{e}")


# Output:

"""
Anika is 34, her ID is 234
Anima is 45, her ID is 561
The file is read..
"""