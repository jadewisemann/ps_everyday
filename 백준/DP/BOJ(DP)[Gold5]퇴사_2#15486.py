import sys 

def solve():

    data = sys.stdin.read().split()

    n = int(data[0])
    dp = [0] * (n + 1)

    for now in range(n - 1, -1, -1):
        time = int(data[1 + now * 2]) 
        price = int(data[2 + now * 2])

        end_day = now + time

        if end_day <= n:
            do = price + dp[end_day]
            skip = dp[now + 1]
            dp[now] = do if do > skip else skip
        else:
            dp[now] = dp[now + 1]

    print(dp[0])

solve()