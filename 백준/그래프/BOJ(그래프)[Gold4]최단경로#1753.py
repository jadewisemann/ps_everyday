import sys
input = sys.stdin.readline

import heapq

INF = float('inf')

V, E = map(int, input().split())
K = int(input())

grp = [[] for _ in range(V + 1)]
dists = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    grp[u].append((v, w))

q = []
heapq.heappush(q, (0, K))
dists[K] = 0

while q:
    dist, now = heapq.heappop(q)
    
    if dists[now] < dist:
        continue

    for neigbor, weight in grp[now]:
        cost = dist  + weight

        if cost < dists[neigbor]:
            dists[neigbor] = cost
            heapq.heappush(q, (cost, neigbor))


for i in range(1, V + 1):
    print(dists[i] if dists[i] != INF else "INF")