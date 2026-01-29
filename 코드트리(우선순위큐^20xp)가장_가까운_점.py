n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import heapq as hq


min_heap = [(x*y, x, y) for x, y in points]
hq.heapify(min_heap)

for _ in range(m):
    _, x, y = hq.heappop(min_heap)
    hq.heappush(min_heap, ((x + 2) * (y + 2), x + 2, y + 2))

_ , x, y = hq.heappop(min_heap)

print(x, y)