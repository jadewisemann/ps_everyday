def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x, root_y = find(parent, x), find(parent, y)

    if root_x == root_y:
        return False
     
    parent[root_y] = root_x
    return True

def get_mst_cost(v, edges):
    edges.sort()
    
    parent = list(range(v + 1))
    mst_cost = 0
    edges_count = 0
    
    for cost, a, b in edges:
        if union(parent, a, b):
            mst_cost += cost
            edges_count += 1
            
            if edges_count == v - 1:
                break
                
    return mst_cost

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]

edges = []

for i in range(n):
    sx, sy = stars[i]
    for j in range(n):
        if i == j: continue
        ex, ey = stars[j]
        cost = (abs(sx - ex) ** 2 + abs(sy - ey) ** 2) ** 0.5
        edges.append((cost, i, j))

print(f"{get_mst_cost(n, edges):.2f}")
