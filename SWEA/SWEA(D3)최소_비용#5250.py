import heapq


def main():
    n = int(input())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    while pq:
        current_fuel, x, y = heapq.heappop(pq)
        
        if current_fuel > dist[x][y]: continue
            
        if x == n - 1 and y == n - 1: return current_fuel
            
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                height_diff = grid[nx][ny] - grid[x][y]
                new_fuel = current_fuel + 1 + max(0, height_diff)
            
                if new_fuel < dist[nx][ny]:
                    dist[nx][ny] = new_fuel
                    heapq.heappush(pq, (new_fuel, nx, ny))


if __name__ == "__main__":
    for tc in range(int(input())):
        print(f"#{tc + 1} {main()}")


