def bellman_ford(start_node, n, edges):
    dist = [float('inf')] * (n + 1)
    dist[start_node] = 0

    for i in range(n):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                
                if i == n - 1:
                    return True, []

    return False, dist

