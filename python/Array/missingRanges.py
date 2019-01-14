'''
Given a sorted integer array nums, where the range of elements are in the inclusive range
[lower, upper], return its missing ranges.
Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

'''
def getMissingString(first, last):
    if first < last:
        return str(first) + "->" + str(last)
    else:
        return str(first)

def findMissingRanges(arr, lower, upper):
    N = len(arr)

    res = []
    next = lower

    if len(arr) == 0:
        if lower == upper:
            return [ str(lower)]
        else:
            return [str(lower) + "->" + str(upper)]

    for i in range(N):
        if next < arr[i]:
            res.append(getMissingString(next, arr[i]-1))
        next = arr[i] + 1

    if upper != arr[-1]:
        res.append(getMissingString(arr[-1]+1, upper))

    return res



'''
Method 2
    # check is lower is present in arr
    if lower != arr[0]:
        last = arr[0] - 1
        if lower == last:
            res.append(str(lower))
        else:
            res.append(str(lower) + "->" + str(last))

    for i in range(N-1):
        if (arr[i] + 1) != arr[i+1]:
            first = arr[i] + 1
            last = arr[i+1] - 1
            if first == last:
                res.append(str(first))
            else:
                res.append(str(first) + "->" + str(last))

    # check is upper is present in arr
    if upper != arr[-1]:
        first = arr[-1] + 1
        if lower == last:
            res.append(str(upper))
        else:
            res.append(str(first) + "->" + str(upper))
'''


nums = [1, 3, 50, 75]
lower = 0
upper = 99

print(findMissingRanges(nums, lower, upper))
