input_file = 'strawberry.txt'

def main():
    words = []
    try:
        with open(input_file) as filein:
            for w in filein.read().split().strip(","):
             words.append(w)
             

    except OSError:
        print("Açaman gardaşş")

    for i in range(len(words) - 2):
        if len(words[i]) == len(words[i+1]) and len(words[i+1]) == len(words[i+2]):
         print((words[i]), (words[i+1]),(words[i+2]))

if __name__ == "__main__":
    main()