

def lovefunc( flower1, flower2 ):
    return (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)

flower1 = 5
flower2 = 34

result = lovefunc( flower1, flower2 )
print(result)