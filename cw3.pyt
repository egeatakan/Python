dnatorna = {
    'T': 'U',
    'A': 'A',
    'C': 'C',
    'G': 'G'
}
rna = []
def DNAto_RNA(dna,rna):
    for letter in dna:
        rna.append(dnatorna[letter])
    print(str(rna))
    return "".join(rna)


# Örnek DNA dizisi
dna_sequence = "AGCT"

# Fonksiyonu çağır ve RNA dizisini al
DNAto_RNA(dna_sequence, rna)

# RNA dizisini döndürme (ekrana yazdırma yok)
# print(rna_sequence)  # Bu satır sadece değer döndürür, bir işlem yapılmaz.