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
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

AZ1452seats = ["2 1","2 2","2 3","1 2","1 1","1 3" ]
OS316seats =  ["1 1","1 2","1 3","2 1","2 2","2 3","3 1","3 2","3 3" ]
LH1120seats = ["1 1","1 2","2 1","2 2","3 1","3 2"]
AZ1452 = []
OS316 = []
LH1120 = []


bookings = 'bookings.txt'
fligts = 'flights.txt'
Cancels = []
booked = []


#print(open('flights.txt', 'r').read())
#print()
#print(open('bookings.txt', 'r').read())
#print()

def main():
    try:
        with open('bookings.txt', 'r' , encoding='UTF-8') as books:
            for line in books:
                if line.find("BOOK"):
                    Cancels.append(line)
                elif line.find("CANCEL"):
                    booked.append(line)
            for Booked in booked:
            
                if Booked.find("BOOK LH1120") and Booked.find("BOOK OS316"):
                    AZ1452.append(Booked)
                elif Booked.find("BOOK AZ1452") and Booked.find("BOOK LH1120"):
                    OS316.append(Booked)
                elif Booked.find("BOOK AZ1452") and Booked.find("BOOK OS316"):
                    LH1120.append(Booked)
            print("Flight AZ1452:")
            for lh1120list in LH1120 :
                print (lh1120list)
            print("Flight AZ1452:")
            for az1452list in AZ1452:              
                print((az1452list))
            print("Flight OS316:")    
            for os316list in OS316:
                print(os316list)
            print("Cancels:")
            for cancellist in Cancels
                print(Cancels)

    except OSError:
        print("oserror")        




if __name__ == "__main__":
    main()
