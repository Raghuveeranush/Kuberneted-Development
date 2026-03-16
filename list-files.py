import os

folders = input("Please provide the list of folders path:").split

print(folders)
for folder in folders:
    if os.path.exists(folder):
        print(f"Files in {folder}:")
        for file in os.listdir(folder):
            print(file)
    else:
        print(f"{folder} does not exist.") 