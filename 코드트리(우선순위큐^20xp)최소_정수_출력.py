n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
import heapq as hq

min_heap = []

for el in x:
    if el:
        hq.heappush(min_heap, el)   
    else:
        print(hq.heappop(min_heap) if min_heap else 0)