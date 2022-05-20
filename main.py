import matplotlib.pyplot as plt
import numpy as np



import math
import numpy as np
import matplotlib.pyplot as plt
from math import ceil, sqrt
from draw import create_graph
from prime_number import isprime
from add_multi import ecc_add
from variable import a,b,p
from bsgs import bsgs
from count_ecc import count_ecc





ecc_T = []
ecc_test = []
for a in range(-p, p):
    for b in range(-p, p):
        if 4*a**3 + 27*b**2 != 0:
            test = count_ecc(a,b,p) #tổng số điểm của ecc
            ecc_test.append(test)
            #thêm số điểm và các thông số a,b vào mảng
            ecc_T.append([test,a,b])



print("Số thứ nhất thể hiện số điểm")
print("Số thứ hai là a")
print("Số thứ ba là b")
print(ecc_T)
print("Số đường cong cần xét trong trường hợp p =  " ,p )
print(len(ecc_T))

# ecc_test.sort()

# Tim so duong cong co cung so diem trong ecc_test

# occ_dict = {}
# for item in ecc_test:
#    if isprime(item) is True:
#         if item not in occ_dict:
#             occ_dict[item] = 1
#         else:
#             occ_dict[item] += 1
#
#
# print("Số thứ nhất là số điểm trên đường cong")
# print("Số thứ hai là số cặp đường cong có cùng số điểm")
#
#
# for item in occ_dict:
#     print(item,' :',math.comb(occ_dict[item],2))


# print("")
# print("")
# print("Số thứ nhất thể hiện số điểm ")
# print("Số thứ hai thể hiện số đường cong có cùng số điểm ")
# print(occ_dict)
# print(len(ecc_test))
# occ_dict1 = {}
# for item in ecc_test:
#     if item not in occ_dict1:
#         occ_dict1[item] = 1
#     else:
#         occ_dict1[item] += 1
#
# print("Số thứ nhất là số điểm trên đường cong")
# print("Số thứ hai là số cặp đường cong có cùng số điểm")
#
# for item in occ_dict:
#     print(item,' :',math.comb(occ_dict[item],2))
#
# print("")
# print("")
# print("Số thứ nhất thể hiện số điểm ")
# print("Số thứ hai thể hiện số đường cong có cùng số điểm ")
# print(occ_dict1)
# print(len(ecc_test))

# print("All points on ECC: ", ecc_Point)
# count_p = len(ecc_Point)
# print(count_p + 1)

# P = Point(1, 5)
# Q = Point(6, 11)
#
# add_PQ = ecc_add(P, Q)
#
# print("P: ", P)
# print("Q: ", Q)
#
# print("P+Q: ", add_PQ)
#
# index = 2
# X = P
# while True:
#     X = ecc_add(P,X)
#     if index == count_p+2:
#         break
#
#     print(f"{index}P = {X}")
#     index += 1
#


# create_graph(20,a,b)
# find_points(p)
# plt.show()
