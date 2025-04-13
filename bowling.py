import random
import time
sayılar = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def black_check(liste):
    if len(liste) == 2 and "A" in liste and any(kart in ["10", "J", "Q", "K"] for kart in liste):
        return True
    return False


def kart_değeri(kart):
    if kart in ["J","Q","K"]:
        return 10
    elif kart in ["A"]:
        return 11
    else:
        return int(kart)

def kasa_çek(kasa_listesi):
    kasa_listesi.append((random.choice(sayılar)))

def print_kasa(kasa_listesi):  
    print("Kurpiyer:", " , ".join(map(str, kasa_listesi)))

def oyuncu_çek(oyuncu_listesi):
    oyuncu_listesi.append((random.choice(sayılar)))

def print_oyuncu(oyuncu_listesi):  
    print("Oyuncu:", " , ".join(map(str, oyuncu_listesi)))

def hesapla_toplam(liste):
    toplam = sum(kart_değeri(kart) for kart in liste)
    as_sayısı = liste.count("A")
    while toplam > 21 and as_sayısı > 0:
        toplam -= 10
        as_sayısı -= 1
    return toplam

def main():
    balance = 100  
    print("-------------")
    print("EgeBet Blackjack")
    print("-------------")

    while balance > 0:  
        print(f"Mevcut bakiyeniz: ${balance:.2f}")

        bet = input("Bahis miktarını girin: ")

        if not bet.isdigit():
            print("Lütfen geçerli bir sayı girin.")
            continue
     
        bet = int(bet)

        if bet > balance:
            print("Bahis bakiyenizden büyük olamaz.")
            continue
        if bet <= 0:
            print("Lütfen sıfırdan büyük bir bahis girin.")
            continue
     
        balance -= bet 

        # Oyuncunun ve kurpiyerin elini başlat
        oyuncu_listesi = []
        kasa_listesi = []
        

        print("*****************")
        print("Dağıtılıyor... \n")
        time.sleep(1)
        kasa_çek(kasa_listesi)
        print_kasa(kasa_listesi)
        time.sleep(1)
        oyuncu_çek(oyuncu_listesi)
        print_oyuncu(oyuncu_listesi)
        print("*****************")

        time.sleep(1)
        print("Kurpiyer:", " , ".join(map(str, kasa_listesi)), ", X")
        kasa_çek(kasa_listesi)
        time.sleep(1)
        oyuncu_çek(oyuncu_listesi)
        print_oyuncu(oyuncu_listesi)
        print("*****************")
        time.sleep(1)

        if black_check(oyuncu_listesi) and black_check(kasa_listesi):
            print("Beraberlik! Her iki taraf da Blackjack yaptı.")
            print_kasa(kasa_listesi)
            print_oyuncu(oyuncu_listesi)
            print("*****************")
            balance += bet
            continue
        elif black_check(oyuncu_listesi):
            print_kasa(kasa_listesi)
            print_oyuncu(oyuncu_listesi)
            print("*****************")
            print("Blackjack! Oyuncu kazandı!")
            balance = balance + bet + bet + (bet/2)
            continue
        elif black_check(kasa_listesi):
            print_kasa(kasa_listesi)
            print_oyuncu(oyuncu_listesi)
            print("*****************")
            print("Kurpiyer Blackjack yaptı. Kaybettiniz.")
            continue
        time.sleep(1)
        
        seçim = input("Hit/Stand/Double: ").lower()
        while seçim not in ["hit", "stand", "double"]:
             print("Geçersiz seçim! Lütfen 'hit' ya da 'stand' yazınız.")
             seçim = input("Hit/Stand/Double: ").lower()
        while seçim == "hit":
            oyuncu_çek(oyuncu_listesi)
            print("Kurpiyer:",kasa_listesi[0], ", X")
            time.sleep(1)
            print_oyuncu(oyuncu_listesi)
            print("*****************")
            toplam = hesapla_toplam(oyuncu_listesi)
    
            if toplam > 21:
                print("Enayi! Kaybettin.")
                break
        
            seçim = input("Hit/Stand: ").lower()
        
        if seçim == "stand":
            time.sleep(1)
            print_kasa(kasa_listesi)
            print_oyuncu(oyuncu_listesi)
            print("*****************")
            while hesapla_toplam(kasa_listesi) < 16:
                kasa_çek(kasa_listesi)
                print_kasa(kasa_listesi)
                time.sleep(1)
                print_oyuncu(oyuncu_listesi)
                print("*****************")
                time.sleep(1)
        
        if seçim == "double":
            balance -= bet
            bet *= 2
            oyuncu_çek(oyuncu_listesi)
            print("Kurpiyer:",kasa_listesi[0], ", X")
            time.sleep(1)
            print_oyuncu(oyuncu_listesi)
            print("*****************")
            time.sleep(2)
            print_kasa(kasa_listesi)
            print_oyuncu(oyuncu_listesi)
            print("*****************")
            while hesapla_toplam(kasa_listesi) < 16:
                kasa_çek(kasa_listesi)
                print_kasa(kasa_listesi)
                time.sleep(1)
                print_oyuncu(oyuncu_listesi)
                print("*****************")
                time.sleep(1)   

            
        oyuncu_toplam = hesapla_toplam(oyuncu_listesi)
        kasa_toplam = hesapla_toplam(kasa_listesi)
                
        if oyuncu_toplam > 21:
            print("Oyuncu 21'i geçti, kaybettiniz.")
       #elif seçim == "double" and kasa_toplam > 21 or oyuncu_toplam > kasa_toplam:
            #print("Oyuncu double ile kazandı! Tebrikler.")
            #balance += bet * 4
        elif kasa_toplam > 21 or oyuncu_toplam > kasa_toplam:
            print("Oyuncu kazandı! Tebrikler.")
            balance += bet * 2
        elif oyuncu_toplam < kasa_toplam:
            print("Kurpiyer kazandı.")
        else:
            print("Beraberlik.")
            balance += bet

        print(f"Yeni bakiye: ${balance}\n")
        if balance <= 0:
            print("Bakiye bitmiştir, oyun sona erdi.")
            break

if __name__ == '__main__':
    main()
