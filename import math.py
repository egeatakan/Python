import math

a = int(input("a kenarinin uzunluğu kaç cm? :"))
b = int(input("b kenarinin uzunluğu kaç cm? :"))

c=pow(a, 2)
d=pow(b, 2)

S = math.sqrt(c + d)
print(f"Hipotenüsün uzunluğu {S}")