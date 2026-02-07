
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq as hq

max_heap = [-i for i in arr]
hq.heapify(max_heap)

for _ in range(m):
    curr = hq.heappop(max_heap)
    hq.heappush(max_heap, curr + 1)

print(-hq.heappop(max_heap))
