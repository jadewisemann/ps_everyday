n = int(input())
m = int(input())

INF = float('inf')
dists = [[INF] * n for _ in range(n)]

for i in range(n):
    dists[i][i] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    if w < dists[a-1][b-1]:
        dists[a-1][b-1] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dists[i][k] + dists[k][j] < dists[i][j]:
                dists[i][j] = dists[i][k] + dists[k][j]

for i in range(n):
    for j in range(n):
        if dists[i][j] == INF:
            print(0, end=" ")
        else:
            print(dists[i][j], end=" ")
    print()