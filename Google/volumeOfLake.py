# https://techdevguide.withgoogle.com/resources/volume-of-water/#!


def calculateVol(arr, l, h):
    vol = 0
    for i in range(l+1, h):
        vol += (arr[l]-arr[i])
        print(l, i, arr[l], arr[i], vol)
    return vol

def volumeOfLake(arr):
    N = len(arr)
    m = 0
    vol = 0
    # forward pass
    for i in range(N):
        if arr[m] <= arr[i]:
            vol += calculateVol(arr, m, i)
            m = i
    m = N - 1

    # reverse pass
    for i in range(N-1, -1, -1):
        if arr[m] < arr[i]:
            print(range(m-1, i, -1), m, i )
            for j in range(m-1, i, -1):
                vol += (arr[m]-arr[j])
            m = i

    return vol
#print(volumeOfLake([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]))
print(volumeOfLake([1,5,3,4,6,4,5,6]))
