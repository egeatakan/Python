NUMBERS = 'numbers.txt'
ARMSTRONG_NUMBERS = 'armstrong.txt'


def bulucu(number):
    return sum(int(d) ** len(str(number))for d in str(number))

def main():
    try:
        with open(NUMBERS) as inputfile, open(ARMSTRONG_NUMBERS, 'w') as outputfile:
            for line in inputfile:
                number = int(line.strip())  # Satırı temizle ve tamsayıya çevir
                if bulucu(number) == number:  # Armstrong kontrolü
                    outputfile.write(f"{number}\n")
    except OSError as err:
        print("OSERRORRRRR")


if __name__ == '__main__':
    main()  