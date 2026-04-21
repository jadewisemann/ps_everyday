import heapq

def solve_dijkstra():
    n = int(input())    
    grid = [list(map(int, list(input().strip()))) for _ in range(n)]
    
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    while pq:
        time, x, y = heapq.heappop(pq)
        
        if time > dist[x][y]: continue
            
        if x == n - 1 and y == n - 1: return time
            
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                new_time = time + grid[nx][ny]
                if new_time < dist[nx][ny]:
                    dist[nx][ny] = new_time
                    heapq.heappush(pq, (new_time, nx, ny))


from collections import deque

def solve_dial():
    n = int(input())
    grid = [list(map(int, list(input().strip()))) for _ in range(n)]
    
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    
    buckets = [deque() for _ in range(10)]
    buckets[0].append((0, 0))
    
    curr_dist = 0
    
    while True:
        while not buckets[curr_dist % 10]:
            curr_dist += 1
            if curr_dist > n * n * 9: break 
            
        if not buckets[curr_dist % 10]: break
        
        x, y = buckets[curr_dist % 10].popleft()
        
        if curr_dist > dist[x][y]: continue
            
        if x == n - 1 and y == n - 1: return curr_dist
            
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            nx, ny = x + dx, y + dy
            
            if not(0 <= nx < n and 0 <= ny < n): continue

            new_dist = curr_dist + grid[nx][ny]
    
            if new_dist < dist[nx][ny]:
                dist[nx][ny] = new_dist
                buckets[new_dist % 10].append((nx, ny))

if __name__ == "__main__":
    for tc in range(int(input())):
        ans = solve_dial()
        print(f"#{tc + 1} {ans}")