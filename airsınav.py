booking_file = 'booking.txt'
AZ1452_yolcuları = []  # AZ1452 uçuşu için yolcuları saklayacağımız liste
TK2020_yolcuları = []

def get_passengers_for_flight(flight_no,flighyolcular):
    """Belirtilen uçuş numarasına göre yolcuları listeye ekler."""
    try:
        with open(booking_file, 'r') as books:
            for line in books:
                # Satırı parçalayarak uçuş bilgilerini al
                action, flight, name, surname, seat_count = line.strip().split()
                if flight == flight_no and action == "BOOK":  # Yalnızca BOOK işlemlerini al
                    flighyolcular.append(f"{name} {surname}")  # İsim ve soyisim eklenir
                    
    except OSError as e:
        print(f"Booking.txt dosyasını okurken hata oluştu: {e}")

if __name__ == "__main__":
    get_passengers_for_flight("AZ1452",AZ1452_yolcuları)
    print("AZ1452 yolcuları:")
    print(AZ1452_yolcuları)
    get_passengers_for_flight("TK2020",TK2020_yolcuları)
    print("TK2020 Yolcuları")
    print(TK2020_yolcuları)
    