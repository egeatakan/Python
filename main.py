# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` {  } ~ |


#print(open('flights.txt', 'r').read())
#print()
#print(open('bookings.txt', 'r').read())
#print()

FILE_FLIGHTS = "flights.txt"
FILE_BOOKINGS = "bookings.txt"

def flight_info(filename):
    flights = list()
    try:
        with open(filename) as file:
            for line in file:
                dic = dict()
                line = line.strip()
                flight_ID, plane_model, rows, cols = line.split()
                dic["flight_ID"] = flight_ID
                dic["plane_model"] = plane_model
                dic["rows"] = rows
                dic["cols"] = cols
                dic["free_seats"] = int(rows) * int(cols)
                flights.append(dic)


    except OSError as problem:
        exit(f"{file}: {problem}")

    return flights


def booking_info(filename):
    bookings = list()
    try:
        with open(filename) as file:
            for line in file:
                dic = dict()
                line = list(line.strip().split())
                if line[0] == "BOOK":
                    dic["op_code"] =line[0]
                    dic["flight_ID"] =line[1]
                    dic["name"] = line[2]
                    dic["surname"] = line[3]
                    dic["number_of_seats"] = line[4]
                else:
                    dic["op_code"] =line[0]
                    dic["flight_ID"] =line[1]
                    dic["name"] = line[2]
                    dic["surname"] = line[3] 
                bookings.append(dic) 


    

    except OSError as problem:
        exit(f"{file}: {problem}")

    return bookings



def main():
    attendance = list()
    fails = list()
    flights = flight_info(FILE_FLIGHTS)
    bookings = booking_info(FILE_BOOKINGS)


    for booking in bookings:
        for flight in flights:
            dic = dict()
            if booking["flight_ID"] == flight["flight_ID"]:
                if booking["op_code"] == "BOOK":
                    if int(booking["number_of_seats"]) <= int(flight["free_seats"]):
                        flight["free_seats"] = int(flight["free_seats"]) - int(booking["number_of_seats"])
                        if int(booking["number_of_seats"]) <= int(flight["cols"]):
                            flight["cols"] = int(flight["cols"]) - int(booking["number_of_seats"])
                            for i in range(int(booking["number_of_seats"])):

                                dic["row"] = 1
                                dic["col"] = i
                                dic["name"] = booking["name"]
                                dic["surname"] = booking["surname"]
                                attendance.append(dic)
                        else:
                            dic["row"] = 2
                    else:
                        dic["book"] = booking["op_code"]
                        dic["flight_ID"] = flight["flight_ID"]
                        dic["name"] = booking["name"]
                        dic["surname"] = booking["surname"]
                        dic["status"] = "Fail"
                        fails.append(dic)
                



    for fail in fails:
        print(fail)
 
    for record in attendance:
        print(record)



if __name__ == "__main__":
    main()