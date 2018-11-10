def heapify(arr, n, i): # complexity -> Log(n)
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[l] > arr[i]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heapSort(arr): # complexity -> nLog(n)

    n = len(arr)
    for i in range(n-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

print(heapSort([3,5,1,2,8,9,4,0]))
