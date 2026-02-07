import sys
sys.setrecursionlimit(10**8)

m, n = map(int, input().split())
grp = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(x, y):
    if x == m -1 and y == n-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    tmp = 0
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        
        if nx < 0 or m <= nx or ny < 0 or n <= ny:
            continue
        
        if grp[x][y] > grp[nx][ny]:
            tmp += dfs(nx, ny)
    
    dp[x][y] = tmp
    return dp[x][y]

print(dfs(0, 0))