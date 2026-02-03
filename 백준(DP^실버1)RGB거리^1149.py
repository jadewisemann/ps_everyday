n = int(input())
arr = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n + 1)]

dp[1] = arr[1]
for idx in range(2, n+1):
    for jdx in range(3):
        dp[idx][jdx] = min(dp[idx - 1][jdx - 1], dp[idx - 1][jdx - 2]) + arr[idx][jdx]
print(min(*dp[n]))

