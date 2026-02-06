from collections import deque as dq 

n,m = map(int, input().split())

friends = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

kevin_numbers = []

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
    
    kevin_numbers.append(sum(dist for dist in dists if dist > 0))

print(kevin_numbers.index(min(kevin_numbers)) + 1)


            

