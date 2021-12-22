def countSwaps(a):
    m = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                m += 1
                (a[j], a[j + 1]) = (a[j + 1], a[j])
    print("Array is sorted in %s swaps."%m)
    print("First Element:", a[0])
    print("Last Element:", a[-1])
