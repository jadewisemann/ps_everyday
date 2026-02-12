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

def get_mst_cost(v, edges):
    edges.sort()
    
    parent = list(range(v + 1))
    rank = [0] * (v + 1)
    mst_cost = 0
    edges_count = 0
    
    for cost, a, b in edges:
        if union(parent, rank, a, b):
            mst_cost += cost
            edges_count += 1
            
            if edges_count == v - 1:
                break
                
    return mst_cost