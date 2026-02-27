MOD = 10 ** 9

n = int(input())
dp = [[0] * 10] + [[0] + [1] * 9] + [[0] * 10 for _ in range(n)]

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1] % MOD
    for j in range(1, 8 + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD
    dp[i][9] = dp[i - 1][8] % MOD

print(sum(dp[n]) % MOD)
