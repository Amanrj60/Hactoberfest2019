def binarySearch(A, element):
    start = 0
    end = len(A) - 1
    while(start <= end):
        mid = start + (end - start)//2
        if(element == A[mid]):
            return mid
        elif(element < A[mid]):
            end = mid -1

        else:
            start = mid + 1
        
    return -1



A = [1, 2, 4, 5, 6, 7, 8, 9, 10]
x = binarySearch(A, 4)
print(x)
