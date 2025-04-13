# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~


CREATURES_FILENAME = "creatures.csv"
SPELLS_FILENAME = "spells.csv"

from operator import itemgetter

def data_reader(filename):
    try:
        data = []
        with open(filename,"r") as file:
            for row in file:
                data.append(row.strip().split(","))
    except OSError:
        exit("file not found!")
    return data

def main():
    creatures = sorted(data_reader(CREATURES_FILENAME), key=itemgetter(2))
    spells = sorted(data_reader(SPELLS_FILENAME), key=itemgetter(1))

    for creature in creatures:
        print(f"{creature[1]} ({creature[2]}, power = {creature[3]})")
        for spell in spells:
            if spell[3] == creature[0] and spell[2] == "attack":
                print(f"    {spell[1]}:{spell[4]}")

if __name__ == "__main__":
    main()