# Find out the fastest way to locate the largest element in a circular sorted array ?

# 4 5 6 7 8 1 2 3

def findLargest(a, low, high):
    if low == high:
        return a[low]

    mid = abs(high - ((high-low)/2))
    if a[low] < a[mid]:
        return findLargest(a, mid, high)
    elif a[low] > a[mid]:
        return findLargest(a, low, mid-1)
    else:
        return a[low]
a = [4, 5, 6, 7, 1]
print(findLargest(a, 0, 4))
