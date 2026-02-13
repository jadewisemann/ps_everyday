import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[False] * n for _ in range(n)]

for length in range(n):
    for i in range(n - length):
        if nums[i] == nums[i + length]:
            if length < 3 or dp[i + 1][i + length - 1]:
                dp[i][i + length] = True


res = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    res.append(str(int(dp[s - 1][e - 1])))

print("\n".join(res) + "\n") 
