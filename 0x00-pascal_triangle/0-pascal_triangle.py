#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle


"""
#!/usr/bin/python3

'''Module to find Pascal's Triangle integers'''

def pascal_triangle(n):

    '''
    Function to find Pascal's Triangle integers

        Parameters:
            n (int): The number of row's of Pascal's triangle

        Returns:
            pascal_triangle (list): Binary string of the sum of a and b
    '''

    pascal_triangle = list()
    if n <= 0:
        return pascal_triangle
    
    # Add first 1.
    if n > 0:
        pascal_triangle.append([1])

    # Add second line.
    if n > 1:
        pascal_triangle.append([1, 1])

    for i in range(3, n+1):
        pascal_triangle.append([0] * i)

        # Set first and last 1
        pascal_triangle[i-1][0] = 1
        pascal_triangle[i-1][i-1] = 1

        # Calculate middle numbers
        for j in range(1, i-1):
            pascal_triangle[i-1][j] = \
                pascal_triangle[i-2][j-1] + pascal_triangle[i-2][j]

    return pascal_triangle
    """
