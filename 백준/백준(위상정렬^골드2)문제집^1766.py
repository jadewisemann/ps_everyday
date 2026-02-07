import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

degrees = [0] * (n + 1)

grp = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    grp[a].append(b)
    degrees[b] += 1

mnhp = []

for i in range(1, n + 1):
    if degrees[i] == 0:
        heapq.heappush(mnhp, i)

result = []

while mnhp:
    curr = heapq.heappop(mnhp)
    result.append(curr)
    
    for next_node in grp[curr]:
        degrees[next_node] -= 1
        if degrees[next_node] == 0:
            heapq.heappush(mnhp, next_node)

print(*result)
