import random

def kasa_çek():
    sayılar = ["A", "K", "O", "J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    return [random.choice(sayılar) for _ in range(1)]

def oyuncu_çek():
    sayılar = ["A", "K", "O", "J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    return [random.choice(sayılar) for _ in range(2)]

def get_payout():
    pass

def main():
    balance = 100

    print("-------------")
    print("EgeBet Blackjack")
    print("-------------")

    while balance > 0:  
        print(f"Your current balance is ${balance}")

        bet = input("Place your bet: ")

        if not bet.isdigit():
            print("Sayı gir lan")
            continue
     
        bet = int(bet)

        if bet > balance:
            print("Bahis bakiyenden büyük olamaz, eşşeksin!")
            continue
        if bet <= 0:
            print("Düzgün bir sayı gir lan")
            continue
     
        balance -= bet  
        print(f"Bet of ${bet} placed! Remaining balance: ${balance}")

        if balance <= 0:
            print("Tebrikler, tüm paranı bitirdin! Oyun bitti.")
            break

if __name__ == '__main__':
    main()
