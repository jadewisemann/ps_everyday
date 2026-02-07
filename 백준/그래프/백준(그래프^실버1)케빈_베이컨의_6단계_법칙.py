from collections import deque as dq 

n,m = map(int, input().split())

friends = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

min_kevin_number = float('inf')
min_idx = -1

for i in range(1, n + 1):
    dists = [-1] * (n + 1)
    dists[i] = 0
    que = dq([i])

    while que:
        curr = que.popleft()
        for friend in friends[curr]:
            if dists[friend]  == -1:
                dists[friend] = dists[curr] + 1
                que.append(friend)
    
    kevin_number = sum(dist for dist in dists if dist > 0)

    if kevin_number < min_kevin_number:
        min_kevin_number = kevin_number
        min_idx = i

print(min_kevin_number)


            

