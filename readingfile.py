import csv

file_path = "C:/Users/egeat/Desktop/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("file yok")
except PermissionError:
    print("izin yokk")