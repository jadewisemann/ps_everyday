import heapq

def dijkstra(start, n, graph):
    dists = [float('inf')] * (n + 1)
    dists[start] = 0
    min_heap = [(0, start)]
    while min_heap:
        dist, curr = heapq.heappop(min_heap)
        
        if dist > dists[curr]:
            continue

        for neighbor, weight in graph[curr]:
            dist_to_neighbor = dist + weight

            if dist_to_neighbor >= dists[neighbor]:
                continue

            dists[neighbor] = dist_to_neighbor
            heapq.heappush(min_heap, (dist_to_neighbor, neighbor))
    return [dist if dist != float('inf') else 0 for dist in dists]

n, m, x = map(int, input().split())

adj_std = [[] for _ in range(n + 1)]
adj_rev = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    adj_std[s].append((e, w))
    adj_rev[e].append((s, w))


dists_to_x = dijkstra(x, n, adj_rev)
dists_from_x = dijkstra(x, n, adj_std)


print(max(map(lambda a, b: a + b, dists_from_x, dists_to_x)))

