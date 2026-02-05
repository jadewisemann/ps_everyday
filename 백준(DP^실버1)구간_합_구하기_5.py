n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for _ in range(m):
    sx, sy, ex, ey = map(int,input().split())
    
    sums = 0
    for x in range(sx - 1, ex):
        for y in range(sy - 1, ey):
            sums += grid[x][y]
    print(sums)