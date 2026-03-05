n, k = map(int, input().split())
a = list(range(1, n + 1))
res = []
i = -1
delegation = [False] * (n + 1)
while len(res) != n:
    i = (i + k) % n
    if 
    print(f'i is {i}')
    
    res.append(a[i])

print(res)