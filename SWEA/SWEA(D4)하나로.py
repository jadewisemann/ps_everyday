import heapq

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    visited = [False] * n
    pq = [(0, 0)]
    
    total_cost_sq = 0
    count = 0

    while pq:
        dist_sq, now = heapq.heappop(pq)

        if visited[now]: continue
        
        visited[now] = True
        total_cost_sq += dist_sq
        count += 1

        if count == n: break

        for next_node in range(n):
            if visited[next_node]: continue

            l_sq = (x[now] - x[next_node])**2 + (y[now] - y[next_node])**2
            heapq.heappush(pq, (l_sq, next_node))
    
    return round(total_cost_sq * e)


if __name__ == "__main__":
    for tc in range(int(input())):
        print(f"#{tc + 1} {solve()}")