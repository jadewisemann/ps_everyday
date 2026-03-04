import heapq
heappop = lambda x: heapq.heappop(x)
heappush = lambda x, y: heapq.heappush(x, y)

INF = float('inf')

def dijkstra(n, adj, start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    parents = [0] * (n + 1)

    hq = [(0, start)]
    while hq:
        curr_d, curr = heappop(hq)
        
        if curr_d > dist[curr]: continue

        for nxt, d in adj[curr]:
            nxt_d = curr_d + d
            if dist[nxt] <= nxt_d: continue
            heappush(hq, (nxt_d, nxt))
            parents[nxt] = curr
            dist[nxt] = nxt_d

    return dist, parents
        
def traceback(parents, start, end):
    path = []
    curr = end
    
    while curr != start:
        path.append(curr)
        curr = parents[curr]

    path.append(start)
    return path[::-1]

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    start, end = map(int, input().split())

    dist, parents = dijkstra(n, adj, start)
    path = traceback(parents, start, end)

    print(dist[end])
    print(len(path))
    print(*path)

if __name__ == "__main__":
    main()
