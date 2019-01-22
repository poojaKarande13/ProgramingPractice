
def isWordSquare(arr):
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        if len(arr[0]) == 1:
            return True
        return False

    n = len(arr[0][0])
    for w in arr:
        if len(w) != n:
            return False

    for i in range(n):
        for j in range(i):
            if arr[i][j] != arr[j][i]:
                return False
    return True

def wordSquare():
    
