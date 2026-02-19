a, b = input(), input()
na, nb = len(a), len(b)

dp = [[0]* (nb + 1) for _ in range(na + 1)]

for i in range(1, na + 1):
    for j in range(1, nb + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
print(dp[na][nb])

res = []

ci, cj = na, nb
while True:
    if ci == 0 or cj == 0:
        break

    if dp[ci][cj] == dp[ci][cj - 1]:
        cj = cj - 1
    elif dp[ci][cj] == dp[ci - 1][cj]:
        ci = ci - 1
    else:
        res.append(a[ci - 1])
        ci, cj = ci - 1, cj - 1

res.reverse()
print("".join(res))