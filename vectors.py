def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
    """
    matrix = []
    for index1, row1 in enumerate(u):
        for index2, row2 in enumerate(v):
            if index1 == index2:
                 matrix += [row1 + row2]
    return matrix
def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
    """
    matrix = []
    for elemt in v:
        matrix += [elemt * s]  
    return matrix 
def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9 
 
    """
    sm = 0
    matrix = []
    for i1, e1 in enumerate(u):
        for i2, e2 in enumerate(v):
            if i1 == i2:
                matrix += [e1 * e2]
    q = len(matrix)- 1
    while q != -1:
        sm += matrix[q]
        q += -1
    return sm 
if __name__ == '__main__':
   import doctest
   doctest.testmod()  
