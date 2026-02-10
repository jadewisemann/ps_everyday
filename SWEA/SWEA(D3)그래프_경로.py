for tc in range(int(input())):
    v, e = map(int, input().split())
    adjs = [[] for _ in range(v + 1)]
    for _ in range(e):
        s, e = map(int, input().split())
        adjs[s].append(e)
    start, goal = map(int, input().split())

    res = 0
    vis = [False] * (v + 1)
    vis[start] = True
    stck = [start]
    while stck:
        curr = stck.pop()

        if curr == goal:
            res = 1
            break

        for nxt in adjs[curr]:
            if vis[nxt]:
                continue
            stck.append(nxt)
            vis[nxt] = True
     
    print(f'#{tc + 1} {res}')