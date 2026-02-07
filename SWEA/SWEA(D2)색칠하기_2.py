for tc in range(int(input())):
    n = int(input())
    grid = [[0] * 10 for _ in range(10)]

    for _ in range(n):
        sx, sy, ex, ey, clr = map(int, input().split())
        for nx in range(sx, ex + 1):
            for ny in range(sy, ey + 1):
                grid[nx][ny] += clr

    ans = 0
    for x in range(10):
        for y in range(10):
            curr = grid[x][y]
            if curr not in [1, 2]:
                continue
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < 10 and 0 <= ny < 10) or grid[nx][ny] != curr:
                    ans += 1

    print(f"#{tc + 1} {ans}")