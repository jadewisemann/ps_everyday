i = lambda : int(input())

apt = []
arr = []
max_k, max_n = 0, 0

for _ in range(i()):
    k = i()
    n = i()
    arr.append([k, n])

    if k > max_k:
        max_k = k

    if n > max_n:
        max_n = n

apt = [[i + 1 for i in range(max_n)]]


for idx in range(1,max_k+1):
    tmp = []
    for jdx in range(max_n):
        tmp.append(apt[idx-1][jdx] + (tmp[jdx-1] if tmp else 0))
    apt.append(tmp)

for (k, n) in arr:    
    print(apt[k][n-1])