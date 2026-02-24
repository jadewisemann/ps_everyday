INF = float('inf')

n = int(input())

dp = [INF] * (max(6, n + 1))
dp[3], dp[5] = 1, 1

for curr in range(6, n+1):
    dp[curr] = min(dp[curr - 3], dp[curr - 5]) + 1

print(dp[n] if dp[n] != INF else -1)
