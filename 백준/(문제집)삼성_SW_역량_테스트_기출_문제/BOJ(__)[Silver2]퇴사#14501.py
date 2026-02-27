n = int(input())
tps = [tuple(map(int, input().split())) for _ in range(n)]

def recur(i):
    return (
        0 if i >= n else 
        max(tps[i][1] + recur(i + tps[i][0]) if i + tps[i][0] <= n else 0, recur(i + 1))
    )

print(recur(0)) 


