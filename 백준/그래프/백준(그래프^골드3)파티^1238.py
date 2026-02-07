import heapq

INF = float('inf')

def dijkstra(start, n, graph):
    dists = [float('inf')] * (n + 1)
    dists[start] = 0
    hq = [(0, start)]

    while hq:
        dist, curr = heapq.heappop(hq)


n, m, x = map(int, input().split())

grp = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    grp[s].append((e, w))
    grp[e].append((s, w))

dists = [[INF] for _ in range(n + 1)]

hq = []
heapq.heappush(hq, (0, x))
dists[x] = 0

while hq:
    dist, curr = heapq.heappop()

    if dists[curr] < dist:
        continue

    for neigbor, weight in grp[curr]:
        cost = dist + weight

        if cost < dists[neigbor]:
            dists[neigbor] = cost
            heapq.heappush(hq, (cost, neigbor))


    



