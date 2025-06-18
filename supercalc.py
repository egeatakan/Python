INPUT_FILE = 'expressions.dat'

def operation(op,a,b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b

def read_data(filename):
    expressions = list()
    try:
        with open(filename) as file:
            for line in file:
                sol,sag = line.split(':')
                nums = list()
                for num in sol.split():
                    nums.append(int(num))
                ops = sag.split()
                expressions.append((nums,ops))
    except OSError as problem:
        print("zaaa")
    return expressions

def evaluate_expressions(numbers,operators):
    numbers = numbers[::-1]
    for op in operators:
        numbers.append(operation(op,numbers.pop(),numbers.pop()))
    return numbers[0    ]

def main():
    for nums,op in read_data(INPUT_FILE):
        print(evaluate_expressions(nums,op))

if __name__ == "__main__":
    main()