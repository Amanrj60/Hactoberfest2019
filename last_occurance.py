def lastOccur(A, element):
    start = 0
    end = len(A) - 1
    res = -1
    while(start <= end):
        mid = start + (end - start)//2
        if(element == A[mid]):
            res = mid
            start = mid + 1
        elif(element < A[mid]):
            end = mid -1
        else:
            start = mid + 1

    return res


A = [1, 2, 4, 5, 7, 7, 8, 9, 10]
print(lastOccur(A, 7))
