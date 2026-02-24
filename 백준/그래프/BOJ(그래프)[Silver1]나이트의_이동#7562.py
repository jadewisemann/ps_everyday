from collections import deque

def solve():
    l = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    if si == ei and sj == ej:
        return 0

    vis = [[-1 for _ in range(l)] for _ in range(l)]
    q = deque([(si, sj)])
    vis[si][sj] = True
    
    while q:
        ci, cj = q.popleft()
        
        if ci == ei and cj == ej:
            return vis[ci][cj] - 1

        for di, dj in ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-2, -1), (-1, -2)):
            ni, nj = ci + di, cj + dj

            if not (0 <= ni < l and 0 <= nj < l): continue
            if vis[ni][nj] > 0: continue

            q.append((ni, nj))
            vis[ni][nj] = vis[ci][cj] + 1

for _ in range(int(input())):
    print(solve())