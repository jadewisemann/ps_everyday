import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
adjs = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    adjs[s].append(e)
    indegree[e] += 1

queue = deque([])
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

res = []
while queue:
    now = queue.popleft()
    res.append(now)
    for nei in adjs[now]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            queue.append(nei)


print(*res)