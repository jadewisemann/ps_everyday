def solve(n):
    dp = [0, 1, 1, 1, 2, 2] + [0] * n
    for i in range(6, n + 1):
        dp[i] = dp[i - 5] + dp[i - 1]    
    return dp[n]

for _ in range(int(input())):
    print(solve(int(input())))