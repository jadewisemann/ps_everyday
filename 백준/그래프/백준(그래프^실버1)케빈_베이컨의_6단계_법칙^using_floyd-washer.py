n,m = map(int, input().split())

INF = 101
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            via_dist = dist[i][k] + dist[k][j]
            if dist[i][j] > via_dist:
                dist[i][j] = via_dist

min_kevin = INF * n
answer = 0

for i in range(1, n + 1):
    curr_kevin = sum(dist[i][1:])
    
    if curr_kevin < min_kevin:
        min_kevin = curr_kevin
        answer = i

print(answer)