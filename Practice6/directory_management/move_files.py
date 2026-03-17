import shutil
import os

#1 create folder
os.makedirs("backup", exist_ok=True)

#2 move file
if os.path.exists("example.txt"):
    shutil.move("example.txt", "backup/example.txt")
    print("File moved.")