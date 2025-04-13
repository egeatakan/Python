inputfile = 'numbers.txt'
çıkışcı = []

def main():
    try: 
        with open(inputfile) as otuzbir:
            for numbers in otuzbir:
                number = int(numbers.strip())
                if number % 2 == 0:
                    çıkışcı.append(number)

        print(çıkışcı)
    except OSError:
        print("31111")

if __name__ == "__main__":
    main()