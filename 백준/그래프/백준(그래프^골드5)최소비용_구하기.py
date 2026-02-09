import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

junc = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    junc[s].append((w, e))

start_node, end_node = map(int, input().split())

dist = [float('inf')] * (n + 1)
dist[start_node] = 0

min_heap = []
heapq.heappush(min_heap, ((0, start_node)))

while min_heap:
    dst, curr  = heapq.heappop(min_heap)
    
    if dst > dist[curr]:
        continue

    for wei, nei in junc[curr]:
        dst_to_nei = dst + wei

        if dst_to_nei >= dist[nei]:
            continue

        dist[nei] = dst_to_nei
        heapq.heappush(min_heap, (dst_to_nei, nei))

print(dist[end_node])


