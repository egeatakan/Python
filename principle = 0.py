import math
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Anaparayi giriniz: "))
    if principle <= 0:
     print("Anapara 0 dan küçük veya eşit olamaz")

while rate <= 0:
   rate = float(input("Orani giriniz: "))
   if rate <= 0:
      print("Oran 0'dan küçük veya eşit olamaz")

while time <= 0:
   time = float(input("Süreyi giriniz (gün): "))
   if time <= 0:
      print("En az 1 günlük faiz yapilmaktadir.")

A = principle * math.pow(1 + (rate / 100), time)
print(A)