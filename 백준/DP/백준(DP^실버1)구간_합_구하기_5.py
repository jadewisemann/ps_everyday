import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = grid[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]


for _ in range(m):
    sx, sy, ex, ey = map(int,input().split())
    
    result = dp[ex][ey] - dp[sx - 1][ey] - dp[ex][sy - 1] + dp[sx - 1][sy -  1]

    print(result)