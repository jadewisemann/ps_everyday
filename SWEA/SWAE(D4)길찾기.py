for _ in range(10):
    tc, n = map(int, input().split())
    arr = list(map(int, input().split()))

    adjs = [[] for _ in range(100)]
    for i in range(0, len(arr), 2):
        adjs[arr[i]].append(arr[i + 1])
    
    stck, vis = [0], {0}

    while stck:
        curr = stck.pop()
        for nxt in adjs[curr]:
            if nxt not in vis:
                vis.add(nxt)
                stck.append(nxt)

    print(f'#{tc} {int(99 in vis)}')