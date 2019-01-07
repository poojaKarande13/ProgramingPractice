def volumeOfLake(heights):
    N = len(heights)
    left_max = [0 for i in range(N)]
    right_max = [0 for i in range(N)]

    left_max[0] = heights[0]
    for i in range(1, N):
        left_max[i] = max(heights[i], left_max[i-1])

    right_max[N-1] = heights[N-1]
    for i in range(N-2, -1, -1):
        right_max[i] = max(heights[i], right_max[i+1])

    vol = 0
    for i in range(N):
        vol += min(left_max[i], right_max[i]) - heights[i]
    return vol

print(volumeOfLake([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]))
print(volumeOfLake([1,5,3,4,6,4,5,6]))
