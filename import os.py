import os

file_path = "C:/Users/egeat/Desktop/BO"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("that location doesn't exist")