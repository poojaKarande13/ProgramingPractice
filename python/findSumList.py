def binSearch(nums, low, high, elem):
    print(low,high)
    while low <= high:
        mid = int(high - (high-low)/2)
        if nums[low] == elem or nums[high] == elem or nums[mid] == elem:
            print("found ", elem)
            return True
        elif nums[mid] < elem:
            return binSearch(nums, mid+1, high, elem)
        else:
            return binSearch(nums, low, mid-1, elem)
    return False

def threeSum(nums):
    nums = sorted(nums)
    result = []

    for l in range(len(nums)-1,1, -1):
        for j in range(l-1, 0, -1):
            find = 0 - (nums[l]+nums[j])
            if binSearch(nums, 0, j-1, find) != False:
                s = [find, nums[j], nums[l]]
                if s not in result:
                    result.append(s)
    return result

print(threeSum([0,0,0]))
