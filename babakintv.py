uzunluklar = []

while True:
    uzunluk = int(input("uzunlukları gir :"))
    if uzunluk == -1:
      break
    else:
        uzunluklar.append(uzunluk)

def enbüyükikilibulucu_exe(uzunluklar2):
    uzunluklar2_sıralanmış = sorted(uzunluklar2, reverse=True)
    return uzunluklar2_sıralanmış[0], uzunluklar2_sıralanmış[1]

result_maxbulucu  =(enbüyükikilibulucu_exe(uzunluklar))

sıraoftheking =   int(uzunluklar.index(result_maxbulucu[0]))
sıraofthesecond = int(uzunluklar.index(result_maxbulucu[1]))


aradakifark = uzunluklar.index(result_maxbulucu[0]) - uzunluklar.index(result_maxbulucu[1])
print(f"aradaki fark {aradakifark}")
bizelazımolan = aradakifark * result_maxbulucu[1]
print(f"Konteyner Alanı: {bizelazımolan}")

     
def kucukleri_bul(dizi):
    sonuc = []
    for i in range(len(dizi) - 1):
        # Her iki ardışık elemanı karşılaştır ve küçük olanı sonuç listesine ekle
        sonuc.append(min(dizi[i], dizi[i + 1]))
    return sonuc

aralardakifarklar = kucukleri_bul(uzunluklar)
print(aralardakifarklar)
toplam = 0
for i in range(len(aralardakifarklar)):
  toplam += aralardakifarklar[i]

print(f"toplam su miktarı {toplam}")



