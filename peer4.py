
def aid(income, children):
    sub = 0

    if 30000 < income < 40000 and children >= 3:
        sub = children * 1000
        
    elif 20000 < income < 30000 and children >= 2:
        sub = children * 1500
        
    elif income < 20000:
        sub = children * 2000
    return sub


for i in range(9999):    
    income1 = int(input("Enter your income(-1 to quit): $"))
    if income1 == -1:
        print("See You👋👋")
        break
    else:
        children1 = int(input("Enter children number(-1 to quit): "))
        if children1 == -1:
            print("See You👋👋")
            break
        else:
            answer=aid(income1, children1)
            print("💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")
            print(f"💸 Your subsidy total is : ${answer} 💸")
            print("💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")

