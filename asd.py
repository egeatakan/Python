num_pad = ((1 , 2 , 3),
           (4 , 5 , 6),
           (7 , 8, 9 ),
           ("*" , 0 , "#"))
for num in num_pad :
    for kb in num:
     print(kb, end=(" "))
    print() 

while True:
    password = input("Bir şifre belirleyiniz (max 12) :")
    if len(password) <= 10:
       print("Başarıyla şifre oluşturdunuz.")
       break
    else:
       print("Şifre en fazla 10 karakterden oluşabiir.")

while True:
    user_password = input("Giriş yapmak için şifrenizi giriniz.")
    if not user_password == password:
       print("Hatalı giriş denemesi.")
    else:
       print("Başarıyla giriş yaptınız.")

        
