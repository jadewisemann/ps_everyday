n = int(input())
grp = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    grp[parent][child] = weight

# 1차 순회.
vis = [False] * (n + 1)
que = [[1, 0]]

while que:
    curr, dist = que.pop()
    

    for next in grp[curr]:
        if vis[next]:
            continue
        que.append(vis)
    



# 2차 순회.
