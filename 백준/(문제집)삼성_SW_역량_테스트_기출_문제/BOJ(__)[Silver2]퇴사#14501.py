n = int(input())
tps = [tuple(map(int, input().split())) for _ in range(n)]

def recur(i):
    return (
        0 if i >= n else 
        max(tps[i][1] + recur(i + tps[i][0]) if i + tps[i][0] <= n else 0, recur(i + 1))
    )

print(recur(0)) 


n = int(input())
tps = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    time, price = tps[i]
    
    if i + time <= n:
        dp[i] = max(price + dp[i + time], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])