def overlapping(a, b):
    x1=0
    x2 = 2
    y1 = 1
    y2 = 3
    if (a[x1] < b[x1] and b[x1] < a[x2]) or (a[x1] < b[x2] and b[x2] < a[x2]):
        if (a[y2] < b[y1] and b[y1] < a[y1]) or (a[y2] < b[y2] and b[y2] < a[y1]):
            return True
    if (b[x1] < a[x1] and a[x1] < b[x2]) or (b[x1] < a[x2] and a[x2] < b[x2]):
        if (b[y2] < a[y1] and a[y1] < b[y1]) or (b[y2] < a[y2] and a[y2] < b[y1]):
            return True
    return False

print(overlapping([0, 10, 10, 0], [5, 5, 15, 0]))
print(overlapping([0, 2, 1, 1],[-2, -3, 0, 2]))
