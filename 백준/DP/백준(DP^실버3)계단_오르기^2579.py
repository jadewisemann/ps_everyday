n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
dp[0], dp[1] = arr[0], arr[1]

for i in range(2, n + 1):
    dp[i] = max(arr[i - 1] + dp[i - 3], dp[i - 2]) + arr[i]

print(dp[n])