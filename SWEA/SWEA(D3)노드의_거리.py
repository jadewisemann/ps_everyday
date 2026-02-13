from collections import deque

for tc in range(int(input())):
    v, e = map(int, input().split())

    adjs = [[] for _ in range(50 + 1)]
    for _ in range(e):
        start, end = map(int, input().split())
        adjs[start].append(end)
        adjs[end].append(start)
    
    start, goal = map(int, input().split())

    res = 0
    vis = set()

    queue = deque([(start, 0)])
    vis.add(start)
    
    while queue:
        curr, dist = queue.popleft()

        if curr == goal:
            res = dist
            break

        for _next in adjs[curr]:
            if _next in vis:
                continue
            
            queue.append((_next, dist + 1))
            vis.add(_next)

    print(f'#{tc + 1} {res}')