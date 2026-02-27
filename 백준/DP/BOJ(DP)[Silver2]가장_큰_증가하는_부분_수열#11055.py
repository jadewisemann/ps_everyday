n = int(input())
sequence = list(map(int, input().split()))

dp = sequence[:]

for i in range(n):
    dp[i] = max(
        (
            dp[j] 
            for j in range(i)
            if sequence[j] < sequence[i]
        ), 
        default= 0
    )  + sequence[i]

print(max(dp))