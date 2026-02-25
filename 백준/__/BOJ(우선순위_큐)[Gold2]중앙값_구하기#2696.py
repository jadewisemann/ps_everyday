import heapq

def solve():
    n = int(next(it))
    max_heap, min_heap = [], []
    res = []

    for i in range(n):
        value = int(next(it))
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -heapq.heappushpop(min_heap, value))
        else:
            heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -value))

        if i % 2 == 0:
            res.append(-max_heap[0])

    print(len(res))
    for i in range(0, len(res), 10):
        print(*res[i:i+10])

import sys
it = iter(sys.stdin.read().split())

for _ in range(int(next(it))):
    solve()