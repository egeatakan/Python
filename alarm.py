

import threading
import time

def walk_dog(first, last):
    time.sleep(1)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail(first, last):
    time.sleep(4)
    print(f"You get the mail from {first} {last}")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail, args=("Osman", "Güldemir"))
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("finito")