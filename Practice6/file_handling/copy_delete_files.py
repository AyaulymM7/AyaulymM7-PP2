import shutil
from pathlib import Path

file_path = Path("example.txt")
copy_path = Path("example_copy.txt")

#1 copy
shutil.copy(file_path, copy_path)
print("File copied.")

#2 delete copy
if copy_path.exists():
    copy_path.unlink()
    print("Copy deleted.")