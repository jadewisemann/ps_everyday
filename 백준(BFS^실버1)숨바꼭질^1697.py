from collections import deque, defaultdict

n, k = map(int, input().split())

d = defaultdict(int)

queue = deque([n])
d[n] = 0

while queue:
    x = queue.popleft()

    if x == k:
        break

    for nx in [x - 1, x + 1, x * 2]:
        if 0 <= nx <= 100000 and nx not in d:
            d[nx] = d[x] + 1
            queue.append(nx)
    
print(d[k])