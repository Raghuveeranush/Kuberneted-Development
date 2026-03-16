
import os


def list_folders(file_path):
    try:
        files = os.listdir(file_path)
        return files,None
    except FileNotFoundError:
        #print("File not found:",files)
        return None,"Files not found "
    except PermissionError:
        #print("Invalid file name:",files)
        return None,"permission Error"


def main():
    folders_path = input("Enter the folder in list:").split()
    for path in folders_path:
        files,error_message = list_folders(path)
        if files:
            print(f"printing files in folder path: {path}")
            for file in files:
                print(file)
        else:
            print(f"Error in {path}: {error_message}")


if __name__ == "__main__":
    main()

