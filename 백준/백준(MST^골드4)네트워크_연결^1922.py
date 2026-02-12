import heapq 
import sys
input = sys.stdin.readline

def find(parents, x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    root_x, root_y  = find(parents, x), find(parents, y)

    if  root_x == root_y:
        return Falsez

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y
    return True
    

n, m = int(input()), int(input())
edges = []

for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(edges, (w, s, e))

parents = list(range(n + 1))
mst_cost = 0
edges_used = 0

while edges:
    w, s, e = heapq.heappop(edges)

    if union(parents, s, e):
        mst_cost += w
        edges_used += 1
    
        if edges_used == n - 1:
            break

print(mst_cost)