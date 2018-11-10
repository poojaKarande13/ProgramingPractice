# Find a triplet a, b, c such that a2 = b2 + c2.
# Variations of this problem like find a triplet with sum equal to 0.
# Find a pair with given sum. All such questions are efficiently solved using hashing. – Practice here

# solution
# 1. sort the arr in asc order
# 2. consider a = last element in the arr
# 3. find b and c whose sum is equal to a from the remaining item in the array
# 4. repeat the same step for all elements
# 5. return if b and c found

# complexity O(n2)
def findTriplet(arr):
    n = len(arr)
    arr = sorted(arr)
    for i in range(n-1, 1, -1):
        a = arr[i]
        l = 0
        r = i-1
        while l < r:
            if arr[l] + arr[r] == arr[i]:
                return arr[l], arr[r], arr[i]
            elif arr[l] + arr[r] > arr[i]:
                r -= 1
            else:
                l += 1

print(findTriplet([3,5,6,2,8,9,4]))
