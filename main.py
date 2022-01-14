import matplotlib.pyplot as plt
import numpy as np
import sys

import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple


def create_graph(size, a, b):
    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = -size, size, -size, size
    ticks_frequency = 5

    # Plot points
    fig, ax = plt.subplots(figsize=(10, 10))

    # Set identical scales for both axes
    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax + 1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    # Draw elliptic curve
    ax.set_title(" Elliptic Curve \n \n")
    y, x = np.ogrid[xmin:xmax:0.01, ymin:ymax:0.01]
    plt.contour(
        x.ravel(), y.ravel(), y ** 2 - x ** 3 - a * x - b, [0])


def find_points(p):
    # Find all points ECC mod p
    x1 = []
    y1 = []
    for i in range(p):
        mod_x = (i ** 3 + a * i + b) % p
        for j in range(int(p)):
            if (j ** 2) % p == mod_x:
                if j == 0:
                    y1.append(j)
                    x1.append(i)
                    break
                else:
                    y1.append(j)
                    x1.append(i)
                    y1.append(p - j)
                    x1.append(i)
                break

    plt.scatter(x1, y1)

# Point addition

Point = namedtuple("Point", "x y")
O = "Infinity"


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
                dydx = (3 * P.x ** 2 + a) * inverse_mod_p(2 * P.y)
            else:
                dydx = (Q.y - P.y) * inverse_mod_p(Q.x - P.x)
            x = (dydx ** 2 - P.x - Q.x) % p
            y = (dydx * (P.x - x) - P.y) % p

            result = Point(x, y)
        return result


p = 17
a = 0
b = 7
ecc_Point = []
for i in range(p):
    mod_x = (i ** 3 + a * i + b) % p
    for j in range(int(p)):
        if (j ** 2) % p == mod_x:
            if j == 0:
                ecc_Point.append([i, j])
                break
            else:
                ecc_Point.append([i, j])
                ecc_Point.append([i,p-j])
            break
print("All points on ECC: ", ecc_Point)
count_p = len(ecc_Point)

P = Point(1, 5)
Q = Point(2, 10)

add_PQ = ecc_add(P, Q)

print("P: ", P)
print("Q: ", Q)

print("P+Q: ", add_PQ)

index = 2
X = P
while True:
    X = ecc_add(P,X)
    if index == count_p+2:
        break

    print(f"{index}P = {X}")
    index += 1



# create_graph(20,a,b)
# find_points(p)
# plt.show()
