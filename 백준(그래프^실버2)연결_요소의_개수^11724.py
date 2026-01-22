def dfs(i):
    stk = [i]
    vis[i] = True
    
    while stk:
        curr = stk.pop()
        
        for n in grp[curr]:
            if vis[n]:
                continue
            vis[n] = True
            stk.append(n)


n, m = map(int, input().split())
vis =  [False] * (n + 1)

grp = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    grp[a].append(b)
    grp[b].append(a)
count = 0

for i in range(1, n + 1):
    if not vis[i]:
        dfs(i)
        count += 1

print(count)

