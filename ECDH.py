from add_multi import *
from math import sqrt
from variable import *
def genPA(na,genr):
    g2=genr
    for k in range(1,na):
        g2=ecc_add(g2,genr)
    return g2

def encrypt(Pm,na):
    genr=Point(g,h)
    pa=genPA(na,genr)
    c1=genPA(k,genr)
    c2=genPA(k,pa)
    c2=ecc_add(c2,Pm)
    return c1,c2

def decrypt(na,a3,a4):
    h1=genPA(na,a3)
    # print(-h1.y)
    # Z = Point(h1.x, -h1.y)
    # print(Z)
    h5 = Point(h1.x, p - h1.y)

    h2=ecc_add(a4,h5)
    return h2

if __name__ == "__main__":
    # input d
    g = 3
    h = 193
    # P(g,h) is generator point

    Pm=Point(801, 802)
    # Pm is a point with pm.x is message
    # message is 801

    nb = 2001 # nb is bob's private key
    k = 247247 # alice's private key

    a3,a4=encrypt(Pm,nb)
    print("Message : ", Pm.x)
    print("Alice's private key:", k)
    print("Bob's private key : ", nb)
    print("Bob's public key :", genPA(nb,Point(g,h)))

    print("Encode: ")
    print((a3.x,a3.y),(a4.x,a4.y))
    a6=decrypt(nb,a3,a4)
    print("Message: ")
    print(a6.x,a6.y)
