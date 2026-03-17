from pathlib import Path

file_path = Path("example.txt")

with open(file_path, "w") as f:
    f.write("Hello, this is first line\n")
    f.write("Python file handling practice\n")

print("File created and written.")