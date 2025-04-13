import json
import csv

employess =[["Name","Age","Job"],
           ["Spongebob",30,"Cook"],
           ["Göktuğ",20,"Engineer"],
           ["Tuğberk",16,"Chessçi"]]

file_path = "C:/Users/egeat/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        write = csv.writer(file)
        for row in employess:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("That File already exist!")