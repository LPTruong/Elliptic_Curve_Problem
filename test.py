from math import sqrt
from add_multi import *
from variable import *
from collections import namedtuple
Point = namedtuple("Point", "x y")
mod = p

P = Point(0,0)

def pointAddition(P, Q , a, b, mod):
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
                dydx = (3 * P.x ** 2 + a) * inverse_mod_p(2 * P.y)
            else:
                dydx = (Q.y - P.y) * inverse_mod_p(Q.x - P.x)
            x = (dydx ** 2 - P.x - Q.x) % p
            y = (dydx * (P.x - x) - P.y) % p

            result = Point(x, y)
        return result

def applyDoubleAndAddMethod(P, k, a, b, mod):

    X = P

    kAsBinary = bin(k)  # 0b1111111001
    kAsBinary = kAsBinary[2:len(kAsBinary)]  # 1111111001
    # print(kAsBinary)

    for i in range(1, len(kAsBinary)):
        currentBit = kAsBinary[i: i + 1]
        # always apply doubling
        X = pointAddition(X, X, a, b, mod)

        if currentBit == '1':
            # add base point
            X = pointAddition(X, P, a, b, mod)

    return X


Q = applyDoubleAndAddMethod(P, mod + 1, a, b, mod)
print("(mod + 1)P = ", mod + 1, "P = ", Q)

m = int(sqrt(sqrt(mod))) + 1
print("1 + (mod^1/4) = 1 + (", mod, ")^1/4 = ", m)
print()

terminate = False

for j in range(1, m+1):

    jP = applyDoubleAndAddMethod(P, j, a, b, mod)
    print(j, "P = ", jP, ": ", end="")

    for k in range(-m, m+1):

        checkpoint = applyDoubleAndAddMethod(P, m * 2 * k, a, b, mod)
        checkpoint = pointAddition(checkpoint,Q, a, b, mod)
        print(checkpoint, " ", end="")

        if checkpoint[0] == jP[0]:  # check x-corrdinates of checkpoint and jP
            orderOfGroup = mod + 1 + m * 2 * k

            print("\norder of group should be ", orderOfGroup, " ± ", j)

            try:
                applyDoubleAndAddMethod(P, orderOfGroup + j, a, b, mod)
            except:
                    orderOfGroup = orderOfGroup + j
                    terminate = True
                    break

            try:
                applyDoubleAndAddMethod(P, orderOfGroup - j, a, b, mod)
            except:
                    orderOfGroup = orderOfGroup - j
                    terminate = True
                    break

    print()
    if terminate == True:
        break

print("order of group: ", orderOfGroup)