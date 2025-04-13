SEQUENCE_FILE = 'seq.dat'

def openfile(filename):
    sequences = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                seq = [for int(elem) in line.split()]
                sequences.append(seq)
    except OSError as problem:
        print(f"Eyvah sorun var: {problem}")
    return sequences

def munodi(num):
    c = [num]
    while num > 1:
        if num % 2 == 0:
            num = num // 2  # integer division
        else:
            num = num * 3 + 1
        c.append(num)
    return c

def main():
    sequences = openfile(SEQUENCE_FILE)
    for num, seq in enumerate(sequences):
        if seq == munodi(seq[0]):
            print(f"Sequence {num+1} is a Munodi sequence (length {len(seq)})")
        else:
            print(f"Sequence {num+1} is NOT a Munodi sequence")

if __name__ == "__main__":
    main()
