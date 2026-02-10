def dfs(curr, goal, adjs, vis):
    vis.add(curr)
    return (
        curr == goal 
        or any(
            dfs(nxt, goal, adjs, vis) 
            for nxt in adjs[curr]
            if nxt not in vis
        )
    )

for tc in range(int(input())):
    v, e = map(int, input().split())  

    adjs = [[] for _ in range(v + 1)]
    for _ in range(e):
        u, v = map(int, input().split())
        adjs[u].append(v)

    print(f'#{tc + 1} {int(dfs(*map(int, input().split()), adjs, set()))}')