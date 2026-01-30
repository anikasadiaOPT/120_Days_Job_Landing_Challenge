# Buffering
import os

data = "The people should be so kind because no one is 100% perfect."
path = "Challenge_07.txt"

if os.path.exists(path):
    with open(path, "w") as file:
        file.write(data)
        file.flush()
else:
    print("The file doesn't exists.")