import heapq

def dijkstra(start, adjs, N):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, now = heapq.heappop(pq)
        
        if dist[now] < d:
            continue
            
        for next_node, weight in adjs[now]:
            cost = d + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    return dist

def main():
    n, m, x = map(int, input().split())
    
    adjs = [[] for _ in range(n + 1)]      
    rev_adjs = [[] for _ in range(n + 1)]  
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        adjs[u].append((v, w))
        rev_adjs[v].append((u, w))
    
    to_home = dijkstra(x, adjs, n)
    to_party = dijkstra(x, rev_adjs, n)
    
    max_time = 0
    for i in range(1, n + 1):
        if to_home[i] != float('inf') and to_party[i] != float('inf'):
            max_time = max(max_time, to_home[i] + to_party[i])
            
    return max_time


if __name__ == "__main__":
    for tc in range(int(input())):
        print(f"#{tc + 1} {main()}")
