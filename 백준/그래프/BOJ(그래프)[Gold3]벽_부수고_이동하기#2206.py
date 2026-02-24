from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

visited[0][0][0] = 1
que = deque([(0, 0, False)])

ans = -1

while que:
    sx, sy, isWallBroken = que.popleft()
    
    if sx == n - 1 and sy == m - 1:
        ans = visited[sx][sy][int(isWallBroken)]
        break

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = sx + dx, sy + dy
        curr = int(isWallBroken)
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if (grid[nx][ny] == '1' 
            and not isWallBroken
            and not visited[nx][ny][1]
        ):
            visited[nx][ny][1] = visited[sx][sy][0] + 1
            que.append((nx, ny, True))
        
        elif grid[nx][ny] == '0' and not visited[nx][ny][curr]:
            visited[nx][ny][curr] = visited[sx][sy][curr] + 1
            que.append((nx, ny, isWallBroken))

print(ans)