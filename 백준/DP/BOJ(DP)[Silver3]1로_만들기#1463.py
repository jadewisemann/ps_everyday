n = int(input())
dp = [0] * (n + 1)

for curr in range(2, n + 1):
    dp[curr] = dp[curr - 1] + 1

    if curr % 2 == 0:
        dp[curr] = min(dp[curr], dp[curr // 2] + 1)

    if curr % 3 == 0:
        dp[curr] = min(dp[curr], dp[curr // 3] + 1)

print(dp[n])