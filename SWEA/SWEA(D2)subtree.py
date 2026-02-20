from collections import deque

for tc in range(int(input())):
    e, n = map(int, input().split())
    raw = iter(map(int, input().split()))
    adjs = [[] for _ in range(e + 2)]
    for _ in range(e):
        adjs[next(raw)].append(next(raw))

    q = deque([n])
    cnt  = 0
    while q:
        now = q.popleft()
        cnt += 1
        for nxt in adjs[now]:
            q.append(nxt)
    
    print(f'#{tc + 1} {cnt}')