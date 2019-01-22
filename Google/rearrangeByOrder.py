def shiftRight(arr, i, shift):
    if shift == 0:
        return arr

    j = i
    while j < shift + i:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        j += 1
    return arr

def rearrange(heights, inFront):
    finalOrder = sorted(heights)
    map = {}

    for i in range(len(heights)):
        map[heights[i]] = inFront[i]

    for i in range(len(finalOrder)-1, -1, -1):
        finalOrder = shiftRight(finalOrder, i, map[finalOrder[i]])

    return finalOrder

print(rearrange([5, 2, 3, 6, 1, 4], [0, 1, 1, 0, 1, 2]))
