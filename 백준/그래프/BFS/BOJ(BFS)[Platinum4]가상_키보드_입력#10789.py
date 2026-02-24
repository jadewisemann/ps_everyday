import collections
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().strip().split())
    grid = [list(input().strip()) for _ in range(n)]

    dr = [-1,  1,  0,  0]
    dc = [ 0,  0, -1,  1]

    preproc_grid = [[[] for _ in range(m)] for _ in range(n)]

    for r in range(n):
        for c in range(m):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                while (
                    (0 <= nr < n and 0 <= nc < m)
                    and  (grid[nr][nc] == grid[r][c])
                ):
                    nr += dr[i]
                    nc += dc[i]

                if 0 <= nr < n and 0 <= nc < m:
                    preproc_grid[r][c].append((nr, nc))
                else:
                    preproc_grid[r][c].append(None)


    target = input().strip() + "*"

    vis = [[-1] * m for _ in range(n)]

    q = collections.deque([(0, 0, 0, 0)])

    while q:
        r, c, idx, dist = q.popleft()

        if grid[r][c] == target[idx]:
            if idx == len(target) - 1:
                print(dist + 1)
                return

            if vis[r][c] < idx + 1:
                vis[r][c] = idx + 1
                q.appendleft((r, c, idx + 1, dist + 1))
        
        for nxt in preproc_grid[r][c]:
            if nxt:
                nr, nc = nxt
                if vis[nr][nc] < idx:
                    vis[nr][nc] = idx
                    q.append((nr, nc, idx, dist + 1))
                    

solve()