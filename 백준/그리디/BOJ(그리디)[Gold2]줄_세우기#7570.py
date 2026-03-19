n = int(input())
dp = [0] * (n + 1)

for x in list(map(int, input().split())): 
    dp[x] = dp[x - 1] + 1    
    
print(n - max(dp))
