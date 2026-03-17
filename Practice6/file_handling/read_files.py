from pathlib import Path

file_path = Path("example.txt")

with open(file_path, "r") as f:
    print("Read all:")
    print(f.read())

with open(file_path, "r") as f:
    print("Read line:")
    print(f.readline())

with open(file_path, "r") as f:
    print("Read lines list:")
    print(f.readlines())