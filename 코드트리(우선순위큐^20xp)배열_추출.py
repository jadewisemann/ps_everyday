n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
import heapq as hq

mxh = []
for a in x:
    if a:
        hq.heappush(mxh, -a)
    else:
        print(-hq.heappop(mxh) if mxh else 0)