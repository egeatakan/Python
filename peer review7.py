
girdi = input("Enter positive integers separated by ':': ")
sayılar = girdi.split(":")
sayılar = [int(sayı.strip()) for sayı in sayılar]

#even numbers
ciftsayılar = []
for sayı in sayılar:
    if sayı % 2 == 0:
        ciftsayılar.append(sayı)

#2 digit numbers
ikibasamaklılar = []
for sayıcık in sayılar:
    if 9<sayıcık<100:
        ikibasamaklılar.append(sayıcık)

#w/o maxmin numbers
min_sayı = min(sayılar)
max_sayı = max(sayılar)
to_remove = [min_sayı,max_sayı]
for item in to_remove:  
    sayılar.remove(item)
    
def cool_title(title):
    return f"\n{'=' * 20} 🎉 {title} 🎉 {'=' * 20}"

# Sonuçları yazdıralım
print(cool_title("RESULTS ARE IN!"))
print("-----------------------------------------------------------------")
print(f"🔥 Excluding the minimum and maximum: {':'.join(map(str, sayılar))}")
print(f"🔥 Only even numbers: {':'.join(map(str, ciftsayılar))}") 
print(f"🔥 Only 2 digit numbers : {':'.join(map(str, ikibasamaklılar))}")
print("-----------------------------------------------------------------")
