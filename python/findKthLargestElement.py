
# Using bubble sort k times
def findKthLargetElement(arr, k):
    if k < 1:
        raise Exception("K cannot be less than 1")

    l = len(arr)
    for i in range(k): # k-1, k-2 ... 0
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]

    return arr[l-k]

print(findKthLargetElement([3,5,2,7,9,4,6,1], 8))
