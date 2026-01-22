import heapq as hq
import sys

data = sys.stdin.read().split()
data_iter = iter(data)

arr = []

try:
    n = int(next(data_iter))
    for _ in range(n):
        a = int(next(data_iter))
        if a == 0:
            print(hq.heappop(arr) if arr else 0)
        else:
            hq.heappush(arr, a)
except StopIteration:
    pass



