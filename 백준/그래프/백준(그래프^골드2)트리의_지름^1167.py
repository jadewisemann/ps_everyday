from collections import deque
import sys
input = sys.stdin.readline

def bfs(adj, start, n):

    dists = [-1] * (n + 1)
    que = deque([(start)])

    dists[start] = 0
    max_dist = 0
    farthest_node = start

    while que:
        now  = que.popleft()

        for next_node, weight in adjs[now]:
            if dists[next_node] != -1:
                continue

            dists[next_node] = dists[now] + weight
            que.append(next_node)

            if dists[next_node] > max_dist:
                max_dist = dists[next_node]
                farthest_node = next_node
    
    return farthest_node, max_dist

V = int(input())

adjs = [[] for _ in range(V + 1)]

for _ in range(V):
    node, *data, _ = map(int, input().split())
    adjs[node] = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        
farthest_node, _ = bfs(adjs, 1, V)
_, max_dist = bfs(adjs, farthest_node, V)

print(max_dist)