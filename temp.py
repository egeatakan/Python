yemekler = []
fiyatlar = []
total = 0 

while True:
    yemek = input("Yemeği giriniz :")
    if yemek.lower() == "q":
        break
    else:
        fiyat = float(input("Fiyatı Girin :"))
        yemekler.append(yemek)
        fiyatlar.append(fiyat)
        total += fiyat  # Toplam fiyatı güncelle

print("---------SEPETİNİZ---------")

for i in range(len(yemekler)):
    print(f"{yemekler[i]}: {fiyatlar[i]} TL")

print(f"Toplam Tutar: {total} TL")
