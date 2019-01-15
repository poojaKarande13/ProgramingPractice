def getMaxArea(hist):
    maxArea = 0
    stack = []
    i = 0
    while i < len(hist):
        if len(stack) == 0 or stack[-1] < hist[i]:
            stack.append(i)
            i += 1
        else:
            tp = stack.pop()
            # for tp as height find the area of the rectange
            area = hist[tp] * ((i-stack[-1]-1) if len(stack)>0  else i)
            maxArea = max(maxArea, area)

    while len(stack) > 0:
        tp = stack.pop()
        area = hist[tp] * ((i - stack[-1] -1) if len(stack) > 0  else i)
        maxArea = max(maxArea, area)

    return maxArea

def largestReact(mat):
	maxArea = 0
	arr = [0 for i in range(len(mat))]
	for row in range(len(mat)):
		for col in range(len(mat)):
			if mat[row][col] == 1:
				arr[col] += 1
			else:
				arr[col] = 0
		maxArea = max(maxArea, getMaxArea(arr))

	return maxArea

print(largestReact([[ 1, 1, 1], [0, 1, 1],[1, 0, 0]]))


print(largestReact([
      [0, 1, 1, 1],
      [1, 0, 1, 0],
      [0, 1, 1, 1],
      [1, 1, 1, 1]]))
