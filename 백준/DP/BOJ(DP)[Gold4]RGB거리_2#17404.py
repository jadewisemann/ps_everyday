INF = float('inf')

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

ans = INF

for first in range(3):
    r, g, b = INF, INF, INF
    if first == 0:r = costs[0][0]
    elif first == 1: g = costs[0][1]
    else: b = costs[0][2]

    for i in range(1, n):
        nr = min(g, b) + costs[i][0]
        ng = min(r, b) + costs[i][1]
        nb = min(r, g) + costs[i][2]
        r, g, b = nr, ng, nb

    for last in range(3):
        if first != last:
            ans = min(ans, [r, g, b][last])

print(ans)