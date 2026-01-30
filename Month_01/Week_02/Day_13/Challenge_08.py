# Pathlib

from pathlib import Path

folder = Path("folders")
filename = "Challenge_08.txt"

full_path = folder / filename
print(full_path)


# Output:
"""folders\Challenge_08.txt"""