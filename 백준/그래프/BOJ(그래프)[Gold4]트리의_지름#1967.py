from collections import deque

n = int(input())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

# 한쪽으로 탐색 => 가장 깊은 깊이 == 한쪽 끝
# 그쪽 끝에서 다시 진행

dists = [-1] * (n + 1)
dq = deque([1])
dists[1] = 0

while dq:
    curr =  dq.popleft()
    
    if not tree[curr]:
        continue
    
    for next, weight in tree[curr]:
        if dists[next] != -1:
            continue
        dq.append(next)
        dists[next] = dists[curr] + weight

end = dists.index(max(dists))
dists = [-1] * (n + 1)
dq = deque([end])
dists[end] = 0

while dq:
    curr =  dq.popleft()
    
    if not tree[curr]:
        continue
    
    for next, weight in tree[curr]:
        if dists[next] != -1:
            continue
        dq.append(next)
        dists[next] = dists[curr] + weight

print(max(dists))



