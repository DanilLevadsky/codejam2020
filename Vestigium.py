import numpy as np

tests = int(input())

def solve():
    size = int(input())
    array = []
    for i in range(size):
        array.append([int(x) for x in input().split(" ")])
    matrix = np.array(array)
    k = np.trace(matrix)
    r = sum( len(set(row)) != size for row in matrix )
    c = sum( len(set(column)) != size for column in matrix.T )
    return "{} {} {}".format(k, r, c)
    
for x in range(tests):
    result = solve()
    print("Case #{}: {}".format(x+1, result))
