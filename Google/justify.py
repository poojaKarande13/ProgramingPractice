def justify(arr, L):
    countTotal = 0
    for word in arr:
        countTotal += len(word)

    totalSpacesToAllot = L - countTotal

    spaceBetween = totalSpacesToAllot / (len(arr) - 1)
    remainSpaces = totalSpacesToAllot % (len(arr) - 1)
    res = arr[0]
    for i in range(1, len(arr)):
        res += " " * spaceBetween + " " * remainSpaces + arr[i]
        remainSpaces = 0
    return res

def leftJustified(arr, L):
    res = arr[0]
    for i in range(1, len(arr)):
        res += " " + arr[i]

    remainingSpaces = L - len(res)
    res += " " * remainingSpaces
    return res

def main(arr, L):
    res = []
    i = 0
    j = 0

    count = 0
    while j < len(arr):
        if len(arr[j]) + count  + 1 > L:
            res.append(justify(arr[i:j], L))
            i = j
            count = 0
        else:
            count += 1 + len(arr[j])
            j += 1

    if i == j:
        res.append(leftJustified([arr[i]], L))
    else:
        res.append(leftJustified(arr[i:j], L))

    return res

print(main(["This", "is", "an", "example", "of", "text", "justification."], 16))
