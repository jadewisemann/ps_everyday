import heapq as hq

n, k = map(int, input().split())

jewels = sorted([ 
    list(map(int, input().split()))
    for _ in range(n)
])

bags = sorted([
    int(input())
    for _ in range(k)
])

result = 0
tmp_jewels = []
idx = 0

for bag in bags:
    while idx < n and jewels[idx][0] <= bag:
        hq.heappush(tmp_jewels, -jewels[idx][1])
        idx += 1

    if tmp_jewels:
        result += -hq.heappop(tmp_jewels)

print(result) 
