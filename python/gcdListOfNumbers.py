def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcdList(arr, num):
    result = arr[0]
    for i in range(1, num):
        if result > arr[i]:
            result = gcd(result, arr[i])
        else:
            result = gcd(arr[i], result)

    return result

print(gcdList([4,8,10], 3))
