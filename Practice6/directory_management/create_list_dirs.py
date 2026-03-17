import os

#1 create folders
os.makedirs("test_dir/sub_dir", exist_ok=True)

#2 list files
print("Files in current dir:")
print(os.listdir("."))

#3 current directory
print("Current directory:")
print(os.getcwd())