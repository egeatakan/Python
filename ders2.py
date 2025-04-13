cumle=input("cumle gir: ") 
def temizleyici(coni):
    temizlenmiş = ' '.join(coni.split())
    return  temizlenmiş

temizcumle=temizleyici(cumle)



def count_words(string):
    c=1
    for letter in string:
        if letter ==" ":
            c+=1
    return c        


result=count_words(temizcumle) 
print(f"Cümle {result} kelime") 