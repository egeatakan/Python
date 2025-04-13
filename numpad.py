num_pad = ((1 , 2 , 3),
           (4 , 5 , 6),
           (7 , 8, 9 ),
           ("*" , 0 , "#"))
ayar_menusu = ("1.Hesap Ayarları",
               "2.Şifre Ayarları",
               "3.Güvenlik Ayarları")
for num in num_pad :
    for kb in num:
     print(kb, end=(" "))
    print() 

while True:
    password = input("Lütfen yalnızca rakamlardan oluşan bir şifre girin: ")
    
    if password.isdigit() and len(password) <= 10:  # sadece rakamlardan oluşuyorsa True döner
        print("Şifre başarıyla oluşturuldu!")
        break
    else:
        print("Hatalı giriş! Şifre sadece rakamlardan ve maksimum 10 karakterden oluşmalıdır. Tekrar deneyin.")

while True:
    user_password = input("Giriş yapmak için şifrenizi giriniz :")
    if user_password == password:
       print("Başarıyla giriş yaptınız.")
       break
    else:
       print("Hatalı giriş denemesi.")

print("Menüye devam etmek için 'e' tuşlayınız.")
menu_giris = input("--->")
if menu_giris.lower() == "e":
    for ayar in ayar_menusu:
        print(ayar)  # Her bir ayarı alt alta yazdırır
    
   


    
    
    

        
