for _ in range(int(input())):

    n, m, w = map(int, input().split())
    
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    hasNegativeCycle = False

    dist = [0] * (n + 1)

    for i in range(n):
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

                if i == n - 1:
                    hasNegativeCycle = True
                    break
        
        if hasNegativeCycle: 
            break
    
    print("YES" if hasNegativeCycle else "NO")

