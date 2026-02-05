n = int(input())
parents  = [1] * (n + 1)
adj = [[] for _ in range(n+1)] 

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

vis = [False] * (n + 1)
q = [1]

while q:
    curr = q.pop()
    for child in adj[curr]:
        if not vis[child]:
            q.append(child)
            parents[child] = curr
            vis[child] = True 
for el in parents[2:]:
    print(el)