def find(parent, x):
    if parent[x] == x: return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        parent[root_y] = root_x

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
    