import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x, root_y = find(parent, x), find(parent, y)

    if root_x == root_y:
        return False
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
    return True

v, e = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(e)]

edges.sort(key=lambda x: x[2])

parent = list(range(v + 1))
rank = [0] * (v + 1)

total_cost = 0
count = 0

for a, b, cost in edges:
    if union(parent, rank, a, b):
        total_cost += cost
        count += 1
        if count == v - 1:
            break

print(total_cost)
