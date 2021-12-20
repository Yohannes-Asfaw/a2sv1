def countingSort(arr):
    y = []
    for i in range(100):
        y.append(0)
    for i in arr:
        y[i] += 1
    return y
