import heapq


def main():
    for tc in range(int(input())):
        n, e = map(int, input().split())
    
        adj = [[] for _ in range(n + 1)]
        for _ in range(e):
            s, e, w = map(int, input().split())
            adj[s].append((e, w))
        
        dist = [float('inf')] * (n + 1)
        dist[0] = 0
        
        pq = [(0, 0)]
        
        while pq:
            d, now = heapq.heappop(pq)
            
            if dist[now] < d: continue
                
            for next_node, weight in adj[now]:
                cost = d + weight
                if cost < dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(pq, (cost, next_node))
        
        print(f"#{tc + 1} {dist[n]}")
        

if __name__ == "__main__":
    main()

