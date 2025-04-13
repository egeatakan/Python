kilo = float(input("Kilonuzu Girin :"))
birim = input("KG or LBS? :")

if birim == "kg" or birim == "KG" or birim == "kilo":
  poundaçevir = kilo * 1.35
  print(f"You are {poundaçevir} pounds")

elif birim == "pounds" or birim == "LBS" or birim == "lbs":
  kiloyaçevir = kilo * 0.7
  print(f"You are {kiloyaçevir} kilograms")

else:
  print("Doğru birim giriniz")
