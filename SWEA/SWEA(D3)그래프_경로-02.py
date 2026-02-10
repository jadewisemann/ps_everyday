

for tc in range(int(input())):
    _, e = map(int, input().split())  
    
    adjs = {}
    for _ in range(e):
        u, v = map(int, input().split())
        adjs.setdefault(u, []).append(v)

    start, goal = map(int, input().split())

    vis, layer = {start}, {start}
    while layer:
        if goal in layer:
            break

        layer = {
            nxt 
            for curr in layer
            for nxt in adjs.get(curr, [])
        } - vis 

        vis |= layer

    print(f'#{tc + 1} {1 if goal in vis else 0}')