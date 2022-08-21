from bsgs import bsgs
from prime_number import isprime
import math
from variable import *

def naive(a, b, p):
    L = [0] * p
    for y in range(0, p):
        L[y ** 2 % p] = L[y ** 2 % p] + 1
    ans = 0
    for x in range(0, p):
        mod_p = x ** 3 + a * x + b
        mod_p = mod_p % p
        ans = ans + L[mod_p]
    return ans + 1
# print("\n\n")
# print(f"Số điểm thuộc đường cong với p = 1019 là : ", naive(a, b , 1019))
# print(f"Số điểm thuộc đường cong với p = 10007 là : ", naive(a, b , 10007))
# print(f"Số điểm thuộc đường cong với p = 844643 là : ", naive(a, b , 844643))
# print(f"Số điểm thuộc đường cong với p = 2475493 là : ", naive(a, b , 2475493))


def binomial(n, r):
    ''' Binomial coefficient, nCr, aka the "choose" function
        n! / (r! * (n - r)!)
    '''
    p = 1
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p

#
# ecc_T = []
# ecc_test = []
# L = [0] * p
# for y in range(0, p):
#     L[y ** 2 % p] = L[y ** 2 % p] + 1
# for a in range(0, p):
#     for b in range(0, p):
#         if 4*a**3 + 27*b**2 != 0:
#             ans = 0
#             for x in range(0, p):
#                 mod_p = x ** 3 + a * x + b
#                 mod_p = mod_p % p
#                 ans = ans + L[mod_p]
#             # test = ans #tổng số điểm của ecc
#             ecc_test.append(ans+1) #thêm số điểm và các thông số a,b vào mảng
#             # ecc_T.append([test,a,b])
ecc_points = []
ecc_detail = []
ecc_107point = []
ecc_139point = []
for a in range(0, p):
    for b in range(0, p):
        if (4*a**3 + 27*b**2)%p != 0:
            rs = naive(a,b,p)
            ecc_points.append(rs)
            ecc_detail.append([rs,a,b])
            if (rs == 107):
                ecc_107point.append([rs,a,b])
            elif (rs == 139):
                ecc_139point.append([rs, a, b])
# Trả về danh sách số điểm thuộc các đường cong đã xét
# print(ecc_points)
# Trả về danh sách bao gồm số điểm , a, b
print(ecc_detail)
print(len(ecc_points))
print(ecc_107point)
print(ecc_139point)

ecc_points.sort()

occ_dict = {}
for item in ecc_points:
   if isprime(item) is True:
        if item not in occ_dict:
            occ_dict[item] = 1
        else:
            occ_dict[item] += 1
print(occ_dict)

occ_dict1 = {}
for item in ecc_points:
    if item not in occ_dict1:
        occ_dict1[item] = 1
    else:
        occ_dict1[item] += 1

print((occ_dict1))
# for item in occ_dict:
#     print(item,' :',binomial(occ_dict[item],2))