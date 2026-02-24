for _ in range(int(input())):
    n = int(input())
    dp = [0, 1, 2, 4] + [-1] * (n + 1 - 4)
    for curr in range(4, n + 1):
        dp[curr] = dp[curr - 1] + dp[curr - 2] + dp[curr - 3]
    print(dp[n])
 
