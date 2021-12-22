def insertionSort1(n, arr):
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                m = arr[j + 1]
                arr[j + 1] = arr[j]
                print(" ".join(list(map(str,arr))))
                arr[j] = m
    print(" ".join(list(map(str,arr))))
