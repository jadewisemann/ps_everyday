from collections import deque

for tc in range(10):
    v, e = map(int, input().split())
    it = iter(map(int, input().split()))
    
    adjs = [[] for _ in range(v + 1)]
    indegree = [0] * (v + 1)

    for _ in range(e):
        a, b = next(it), next(it)
        adjs[a].append(b)
        indegree[b] += 1
    
    candi = deque([])

    for i in range(v):
        i = i + 1
        if indegree[i] == 0:
            candi.append(i)
    
    res = []
    while candi:
        now = candi.popleft()
        res.append(now)

        for nxt in adjs[now]:
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                candi.append(nxt)
    

    print(f'#{tc + 1}', *res)        