'''
1) Create an empty stack.

2) Start from first bar     and do following for every bar hist[i] where i varies from 0 to n-1.
a) If stack is empty or hist[i] is higher than the bar at top of stack     then push  i   to stack.b) If this bar is smaller than the top of stack     then keep removing the top of stack while top of the stack is greater.
Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar.
For hist[tp]     the  left index   is previous (previous to tp) item in stack and  right index   is  i   (current index).

3) If the stack is not empty     then one by one remove all bars from stack and do step 2.b for every removed bar.
'''
def largestReactangle(hist):
    print(hist)
    stack = []
    maxArea = 0
    i = 0
    while i < len(hist):
        if len(stack) == 0 or hist[i] > hist[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            tp = stack.pop()
            m = ((i- stack[-1] -1) if len(stack) > 0 else i )* hist[tp]
            maxArea = max(maxArea, m)
            print('pop ', i, stack,tp, m,  maxArea)

    while len(stack) > 0:
        tp = stack.pop()
        m = ((i- stack[-1] -1) if len(stack) > 0 else i )* hist[tp]
        maxArea = max(maxArea, m)
        print('pop ', i, stack, tp, m,  maxArea)
    return maxArea

print(range(7))
print(largestReactangle([6,2,5,4,5,1,6]))
