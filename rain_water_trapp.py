def waterTrap(A):
    n = len(A)
    mxl = [A[0]]
    mxr = [A[n-1]]
    water = []

    for i in range(1, n):
        mxl.append(max(mxl[i-1] , A[i]))
    for i in range(n-2, -1, -1):
        mxr.append(max(mxr[-1], A[i]))
    print(mxl)
    print(mxr)
    x = mxr[::-1]
    for i in range(n):
        water.append(min(x[i],  mxl[i]) - A[i])
    print(water)

    

    return sum(water)


A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
x = waterTrap(A)
print(x)