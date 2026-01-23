a, b = list(input().split('*'))
idx = len(a)
m = int(b[-1])

for arr in [a + str(i) + b for i in range(10)]:
    tmp = 0
    for weight, el in zip([1, 3] * 6, arr[:-1]): 
        tmp += weight * int(el)
    
    if m == (10 - tmp % 10) % 10:
        print(arr[idx])
        break