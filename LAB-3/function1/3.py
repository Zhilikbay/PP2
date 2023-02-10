def solve(y, x):
    z = 'No solutions!'
    for i in range(y + 1):
        j = y - i
        if 2 * i + 4 * j == x:
            return i, j
    return z,z

y = 35
x = 94
solutions = solve(y, x)
print (solutions)