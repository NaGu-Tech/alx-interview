#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            a = 1
            for j in range(1, i + 1):
                level.append(C)
                a = a * (i - j) // j
            res.append(level)
    return res
"""
def pascal_triangle(n):
    a = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    a[i].append(1)
                else:
                    a[i].append(a[i - 1][j] + a[i - 1][j - 1])
            elif (j == i):
                a[i].append(1)

    return a
n = 5
print(pascal_triangle(n))
"""