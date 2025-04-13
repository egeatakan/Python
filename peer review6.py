# m satır
# n sutün

def masakurucu(m, n, anan=0):
    masa = [[anan] * n for _ in range(m)]
    return masa


def masamodifiyesi(m, n):
    masa = masakurucu(m, n)
    print("I. The table with values of zero (0): ")
    for row in masa:
        print(*row)
    print()

    masa = masakurucu(m, n ,1)
    print("II. All cells with values of one (1): ")
    for row in masa:
        print(*row)
    print()

    masa = [[(i + j) % 2 for j in range(n)] for i in range(m)]
    print("III. The cells by alternating 0 and 1 in a checkerboard pattern: ")
    for row in masa:
        print(*row)
    print()

    print("IV. The cells by alternating 0 and 1 in a checkerboard pattern: ")
    print(*[0]* n)
    masa = [[((i) + j) % 2 for j in range(n)] for i in range(m-2)]
    for row in masa:
        print(*row)
        
    print(*[0]* n)
    print()


    masa = [[(i + (j+1)) % 2 for j in range(n-2)] for i in range(m)]
    print("V. Only the cells in the right and left columns with 1, leaving the rest of the table unchanged: ")
    for row in masa:
        print(1, *row, 1) 
    print()
    print("VI. The sum of all the elements: ", sum(sum(row) for row in masa)+((m*2)))

    

m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))
masamodifiyesi(m, n)

