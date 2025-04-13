import math
r=int(input("enter radius: "))
h=int(input("enter height: "))

def sphere_volume(r):
    kure_hacim = 4/3 * math.pi * pow(r,3)
    return kure_hacim
kure_hacimm=sphere_volume(r)

def sphere_surface(r):
    kure_alan = 4 * math.pi * pow(r,2)
    return kure_alan
kure_alann=sphere_surface(r)

def cylinder_volume(r, h):
    silindir_alan = math.pi * pow(r, 2) * h
    return silindir_alan
silindir_alann=cylinder_volume(r,h)

def cylinder_surface(r, h):
    silindir_yuzey = h * 2 * math.pi * r + 2 * (math.pi * pow(r, 2))
    return silindir_yuzey
silindir_yuzeyy=cylinder_surface(h,r)

def cone_volume(r, h):
    koni_hacim = 1/3 * math.pi * pow(r,2)
    return koni_hacim
koni_hacimm=cone_volume(r,h)

def cone_surface(r, h):
    koni_alan = math.pi * pow(r,2) + math.pi * r * pow(pow(h,2) + pow(r,2), 0.5)
    return koni_alan
koni_alann=cone_surface(r,h)

print("---------------------------------")
print(f"Kürenin Hacmi :10{kure_hacimm:.2f}")
print(f"Kürenin yüzey alanı :{kure_alann:.2f}")
print(f"Silindirin Alanı :{silindir_alann:.2f}")
print(f"Silindirin yüzey alanı {silindir_yuzeyy:.2f}")
print(f"Koninin Hacmi :{koni_hacimm:.2f}")
print(f"Koninin yüzey alanı :{koni_alann:.2f}")
print("---------------------------------")













