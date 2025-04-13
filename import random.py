numbers = input("Type integers seperated by ':' character: ")
print()
def list_integers(numbers):
    print(f"This is the list of integers: {numbers}")
    integers = list(map(int, numbers.split(':')))
   
    print()

    empty_list = []
    for i in integers:
        if i != min(integers) and i != max(integers):
          empty_list.append(i)
    empty_list = ':'.join(map(str, empty_list))
    print(f"Excluding minimum and maximum: {empty_list}")

    print()
   
    empty_list = []
    for i in integers:
        if i % 2 == 0:
          empty_list.append(i)
    empty_list = ':'.join(map(str, empty_list))
    print(f"Even number digit: {empty_list}")

    print()
   
    empty_list = []
    for i in integers:
        if 10 <= i <= 99:
          empty_list.append(i)
    empty_list = ':'.join(map(str, empty_list))
    print(f"2-digit numbers: {empty_list}")

    print()

def main():
   program = list_integers(numbers)
   return program

if __name__ == '__main__':
   main()  
