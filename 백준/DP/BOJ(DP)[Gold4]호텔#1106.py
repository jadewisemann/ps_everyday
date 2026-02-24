c, n = map(int, input().split())
dp = [0] * (c  + 1)

cities = [list(map(int, input().split())) for _ in range(n)]
dp = [0] + [float('inf')] * (c + 100)

for cost, man in cities:
    for i in range(man, c + 101):
        if dp[i - man] + cost < dp[i]:
            dp[i] = dp[i - man] + cost

print(min(dp[c:]))