#!/usr/bin/python3

"""
0. Pascal's Triangle
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n.
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