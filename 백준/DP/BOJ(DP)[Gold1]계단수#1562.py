MOD = 10 ** 9

n = int(input())

dp = [[[0] * (2**10) for _ in range(10)] for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for length in range(2, n + 1):
    for last in range(10):
        for mask in range(2**10):
            new_mask = mask | (1 << last)

            if last > 0:
                dp[length][last][new_mask] = (dp[length][last][new_mask] + dp[length - 1][last - 1][mask]) % MOD
                
            if last < 9:    
                dp[length][last][new_mask] = (dp[length][last][new_mask] + dp[length - 1][last + 1][mask]) % MOD

res = 0
for i in range(10):
    res = (res + dp[n][i][2**10 - 1]) % MOD

print(res)