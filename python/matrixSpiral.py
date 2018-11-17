def incr(r0, c0, R, C, result):
    if r0>=0 and c0>=0 and r0<R and c0<C:
        result.append([r0, c0])

def spiralMatrix(R, C, r0, c0):
    """
    :type R: int
    :type C: int
    :type r0: int
    :type c0: int
    :rtype: List[List[int]]
    """
    result = [[r0,c0]]
    walk = 1
    direction = 1

    while len(result) < (R*C):
        print(r0,c0,len(result))
        if direction == 1:
            for _ in range(walk):
                c0 += 1
                incr(r0, c0, R, C, result)
            direction = 2
        elif direction == 2:
            for _ in range(walk):
                r0 += 1
                incr(r0, c0, R, C, result)
            direction = 3
        elif direction == 3:
            for _ in range(walk):
                c0 -= 1
                incr(r0, c0, R, C, result)
            direction = 4
        elif direction == 4:
            for _ in range(walk):
                r0 -= 1
                incr(r0, c0, R, C, result)
            direction = 1

        if direction == 1:
            for _ in range(walk):
                c0 += 1
                incr(r0, c0, R, C, result)
            direction = 2
        elif direction == 2:
            for _ in range(walk):
                r0 += 1
                incr(r0, c0, R, C, result)
            direction = 3
        elif direction == 3:
            for _ in range(walk):
                c0 -= 1
                incr(r0, c0, R, C, result)
            direction = 4
        elif direction == 4:
            for _ in range(walk):
                r0 -= 1
                incr(r0, c0, R, C, result)
            direction = 1
        walk += 1
    return result

print(spiralMatrix(1,4,0,0))
