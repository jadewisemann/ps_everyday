import heapq as hq

ip = lambda: map(int, input().split())

n, k = ip()

# 보석
jewels = [ ]
for _ in range(n):
    jewels.append([*ip()])


bags = []
for _ in range(k):  
    bags.append(int(input()))


jewels.sort()
bags.sort()

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
