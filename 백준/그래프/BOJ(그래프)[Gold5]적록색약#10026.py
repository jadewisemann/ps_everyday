from collections import deque
def solve():
    def find_area(n, grid, is_color_bindness):
        vis = [[False for _ in range(n)] for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if vis[i][j]: continue
                
                target = grid[i][j]
                if is_color_bindness and (target == "R" or target == "G"):
                    target = "RG"

                vis = bfs(n, grid, vis, i, j, target)
                cnt += 1

        return cnt

    def bfs(n, grid, vis, si, sj, target):
        q = deque([(si, sj)])
        vis[si][sj] = True

        while q:
            ci, cj = q.popleft()
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = ci + di, cj + dj

                if not(0 <= ni < n and 0 <= nj < n): continue
                if vis[ni][nj]: continue
                if grid[ni][nj] in target:
                    q.append((ni, nj))
                    vis[ni][nj] = True

        return vis


    n = int(input())
    grid = [input() for _ in range(n)]
    print(find_area(n, grid, False), find_area(n, grid, True))

def solve_alter():
    def find_area(n, grid):
        vis = [[False for _ in range(n)] for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if vis[i][j]: continue
                bfs(n, grid, i, j, vis)
                cnt += 1
        return cnt

    def bfs(n, grid, si, sj, vis):
        q = deque([(si, sj)])
        vis[si][sj] = True
        target = grid[si][sj]
    
        while q:
            ci, cj = q.popleft()
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = ci + di, cj + dj

                if not(0 <= ni < n and 0 <= nj < n): continue
                if vis[ni][nj]: continue
                if grid[ni][nj] in target:
                    q.append((ni, nj))
                    vis[ni][nj] = True

    n = int(input())
    grid = [input() for _ in range(n)]
    print(find_area(n, grid), end=" ")
    print(find_area(n, [row.replace("G", "R") for row in grid]))

solve_alter()