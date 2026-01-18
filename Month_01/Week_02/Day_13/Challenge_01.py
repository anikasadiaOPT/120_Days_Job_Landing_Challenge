# The Safe Open


with open("Anika.txt", "a") as f:
    f.write("\n Hello World!")

with open("Anika.txt", "r") as f:
    file = f.read()
    print(file)                                  # Output:  Hello World!
