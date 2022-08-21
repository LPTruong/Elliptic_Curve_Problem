
from collections import namedtuple
from variable import a,b,p
import sys

Point = namedtuple("Point", "x y")
O = "Infinity"

# Kiểm tra giá trị đầu vào a, b
def valid(P):
    if P == O:
        return True
    else:
        return (
                (P.y ** 2 - (P.x ** 3 + a * P.x + b)) % p == 0 and
                0 <= P.x < p and 0 <= P.y < p)


def inverse_mod_p(x):
    if x % p == 0:
        print("Impossible inverse")
    return pow(x, p - 2, p)


def check_negative(P):
    if P == O:
        return P
    return Point(P.x, (-P.y) % p)


def ecc_add(P, Q):
    # Kiem tra diem co nam tren ECC khong?
    if not (valid(P) and valid(Q)):
        print("Invalid inputs")
        sys.exit()
    # Kiem tra cac diem dac biet
    while valid(P) and valid(Q) == True:
        if P == O:
            result = Q
        elif Q == O:
            result = P
        elif Q == check_negative(P):
            result = O
        else:
            if P == Q:
                lamda = (3 * P.x ** 2 + a) * inverse_mod_p(2 * P.y)
            else:
                lamda = (Q.y - P.y) * inverse_mod_p(Q.x - P.x)
            x = (lamda ** 2 - P.x - Q.x) % p
            y = (lamda * (P.x - x) - P.y) % p

            result = Point(x, y)
        return result

# Q = Point(1, 12)
#
# # Q.y = -Q.y
# # print(Q.y)
# P = Point(1,5)
# print("Điểm P:", P)
# print("Điểm Q:", Q, "\n")
# add_PQ = ecc_add(P, Q)
# print("Kết quả của phép cộng hai điểm P, Q:" ,add_PQ)
#
# print("Kết quả của phép nhân với điểm ban đầu là P:" , P , "\n")




# index = 1
# X = P
# while True:
#     if index != 1:
#         X = ecc_add(P,X)
#     if index == 2*p:
#         break
#     elif X == "Infinity":
#         print(f"{index}P = {X}")
#     else:
#         print(f"{index}P = {X.x, X.y}" , end= (",   " if(index%4 != 0) else '\n'))
#     index += 1
