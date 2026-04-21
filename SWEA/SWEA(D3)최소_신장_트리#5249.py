def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
        
    return False

for tc in range(int(input())):
    v, e = map(int, input().split())
    edges = [
        list(map(int, input().split()))
        for _ in range(e)
    ]
    edges.sort(key=lambda x: x[2])

    parent = list(range(v + 1))
    total_weight = 0
    count = 0

    for u, v, w in edges:
        if union(u, v):
            total_weight += w
            count += 1
            if count == v:break

    print(f"#{tc+1} {total_weight}")