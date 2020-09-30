def peak(A):
    start = 0
    end = len(A) - 1
    while(start <= end):
        mid = start + (end - start)//2
        if(mid > 0 and mid < len(A)-1):
            if(A[mid] > A[mid-1] and A[mid] > A[mid+1]):
                return A[mid]
            elif(A[mid] < A[mid-1]):
                end = mid -1

            else:
                start = mid + 1

        elif(mid == 0):
            if(A[0] > A[mid]):
                return 0
            else:
                return 1
        elif(mid == len(A)-1):
            if(A[-1] > A[len(A) -2]):
                return len(A)-1
            else:
                return  len(A) -2



A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
print(peak(A))