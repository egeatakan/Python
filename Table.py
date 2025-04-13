def create_table(m, n, val=0):
    table = [[val] * n for _ in range(m)]
    return table

def modify_table(m, n):
    table = create_table(m, n)
    print("Başlangıç Tablosu (0):", *table, sep="\n")

    table = create_table(m, n, 1)
    print("\nTüm Hücreler (1):", *table, sep="\n")

    table = [[(i + j) % 2 for j in range(n)] for i in range(m)]
    print("\nDama Deseni:", *table, sep="\n")

    table[0] = table[-1] = [0] * n
    print("\nÜst ve Alt Sıralar (0):", *table, sep="\n")

    for row in table:
        row[0] = row[-1] = 1
    print("\nSol ve Sağ Sütunlar (1):", *table, sep="\n")

    print("\nToplam Elemanlar:", sum(sum(row) for row in table))

m = int(input("Satır sayısını girin (m): "))
n = int(input("Sütun sayısını girin (n): "))
modify_table(m, n)
