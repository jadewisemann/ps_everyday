while True:
    arr = list(map(int, input().split()))

    if arr == [0, 0, 0]: 
        break
    arr.sort()
    a, b, c = arr

    print('right' if c ** 2 == a ** 2 + b ** 2 else 'wrong')