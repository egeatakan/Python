INPUT_FILE = 'landscape.txt'

def read_picture(filename):
    data = []
    try:
        with open(filename) as file:
            for line in file:
                line2 = line.strip()
                data.append(line2)
    except OSError as problem:
        print("zaaa")
    return data

def get_user_input():
    try:
        coord_str = input("Kordinatları giriniz(örn: 6,1): ")
        x_str,y_str = coord_str.split(',')
        x = int(x_str)
        y = int(y_str)
        size_str = input("Kare boyutunu giriniz: ")
        size  = int(size_str)
        return x,y,size
    except ValueError as problem:
        print("Düzgün sayı gir!")
        return None,None,None

def is_square_valid(picture, x, y, size):
    picture_height = len(picture)
    
    if picture_height == 0:
        return False
    picture_width = len(picture[0])

    if x < 0 or y < 0 or size <= 0:
        return False

    if x + size > picture_width:
        return False
        
    if y + size > picture_height:
        return False

    return True

def main():
    picture = read_picture(INPUT_FILE)
    rows = len(picture)
    columns = len(picture[0])
    print(f"rows:{rows} and columns:{columns}")

    y, x, size = get_user_input()
    if x is None:
        return
    
    if is_square_valid(picture,x,y,size):
        print("Seçili nokta ve alan geçerli.Can calculatable.")
    else:
        print("tk olmaz bu")

    stat = dict()
    for r in range(y,y+size):
        for c in range(x,x+size):
            symbol = picture[r][c]
            if symbol not in stat:
                stat[symbol] = 0
            stat[symbol] += 1

    for s in sorted(stat, reverse=True):
        print(f"{s}-> {stat[s]/size/size*100:4.1f}%")

   

if __name__ == "__main__":
    main()