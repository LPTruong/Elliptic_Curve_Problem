
from variable import *


def count_ecc(a, b, p):
    count = 0
    for i in range(p):
        mod_x = (i ** 3 + a * i + b) % p
        for j in range(int(p)):
            if (j**2)%p == mod_x:
                count += 1
                ecc_Point.append([i, j])

    return count+1
ecc_Point = []
print("\n\n")
print("Số điểm của đường cong là :" , count_ecc(a,b,p), "\n")
# print(ecc_Point)
l = len(ecc_Point)//2
print("Các điểm thuộc đường cong :", end="")
count = 0
for i in range (len(ecc_Point)):
    print(ecc_Point[i], ", ", end="")
    count += 1
    if count ==4:
        print("\n                           ", end="")
        count = 0
        # print("\n")

print("Infinity")
# print(len(ecc_Point))
k = 9
for i in ecc_Point:
    if((i[1]*i[1])%(p**k))==((i[0]**3+a*i[0]+b)%(p**k)):
        print((i[1]*i[1])%(p**k))
        print((i[0]**3+a*i[0]+b)%(p**k))
        print(i)
