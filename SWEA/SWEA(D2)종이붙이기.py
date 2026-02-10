dp = [0, 1, 3]

for tc in range(int(input())):
    length = int(input()) // 10
    for i in range(len(dp), length + 1):
        dp.append(dp[i - 1] + dp[i - 2] * 2)

    print(f'#{tc + 1} {dp[length]}') 