# Pickle(The Warning)

import pickle

info = "The information is provided correctly from original sources.\nNow we have to articulate it to the authority."

with open("Challenge_10.pkl", mode = "wb") as file:
    pickle.dump(info, file)

with open("Challenge_10.pkl", mode = "rb") as updated_file:
    data = pickle.load(updated_file)

print(data)


#Output:
"""
The information is provided correctly from original sources.
Now we have to articulate it to the authority.
"""