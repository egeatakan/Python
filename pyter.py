sayilar = []

while True:
    sayi = input("Bir sayı girin (bitirmek için 'q' ya basın): ")
    if sayi.lower() == 'q':
        break
    else:
         sayilar.append(int(sayi))

def square_sum(sayilar):
      return sum(sayi ** 2 for sayi in sayilar)


karelertoplamm = square_sum(sayilar)
print(karelertoplamm)

