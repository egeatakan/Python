cümle = input("Cümle gir bayvan :")

def lengthOfLastWord(cümle):
    liste = cümle.split()
    return len(liste[-1])

result = lengthOfLastWord(cümle)
print(result)

    