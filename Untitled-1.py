words = []

while True:
    word = input("Kelime Giriniz (q to quit)")
    if word == "q":
        break
    else:
        words.append(word)

def smash(words):
    return " ".join(words)

result = smash(words)
print (result)
    