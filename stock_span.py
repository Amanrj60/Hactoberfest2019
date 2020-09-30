def solve(A):
    s = []
    arr = []
    n = len(A)
    for i in range(n):
        if(len(s) == 0):
            arr.append(-1)
        elif(len(s) > 0 and s[-1][0] >= A[i]) :
            arr.append(s[-1][1])
        elif(len(s) > 0 and s[-1][0] <= A[i]):
            while(len(s) > 0 and s[-1][0] <= A[i]):
                s.pop()
            if(len(s) == 0):
                arr.append(-1)
            else:
                arr.append(s[-1][1])

        s.append((A[i],i))
    for i in range(n):
        arr[i] = i - arr[i]
    return arr


A = [100, 80, 60, 70, 60, 75, 85]
x = solve(A)
print(x)