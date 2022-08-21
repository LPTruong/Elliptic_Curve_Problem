
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple

from variable import a,b,p

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

# Tìm điểm trên trường hữu hạn và vẽ lên đồ thị

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
