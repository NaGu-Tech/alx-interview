#!/usr/bin/python3

"""
0. Pascal's Triangle
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n.
"""
def pascal_triangle(n):
    res = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j] + res[i - 1][j - 1])
            elif (j == i):
                res[i].append(1)

    return res
"""
n = 5
print(pascal_triangle(n))
"""