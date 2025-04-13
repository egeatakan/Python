DENEMEIN = 'deneme.dat'


try:
    with(open(DENEMEIN, 'r'))as file:
        for row in file:
            print(row)
except OSError as problem:
    print(f"asdadas {problem}")

    