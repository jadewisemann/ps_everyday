from collections import deque

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve():
    n, k = map(int, input().split())

    si, sj, ei, ej = 0, 0, 0, 0
    grid = []

    for i in range(n):
        row = list(input())
        grid.append(row)
        for j in range(n):
            if   row[j] == 'X': si, sj = i, j
            elif row[j] == 'Y': ei, ej = i, j
    
    visited = [
        [
            [[False] * (k + 1) for _ in range(4)]
            for _ in range(n)
        ] 
        for _ in range(n)
    ]

    queue = deque([(si, sj, 0, k, 0)])
    visited[si][sj][0][k] = True
    
    while queue:
        ci, cj, d, ck, cnt = queue.popleft()
        
        if ci == ei and cj == ej: return cnt
        
        ni, nj = ci + dirs[d][0], cj + dirs[d][1]
        if 0 <= ni < n and 0 <= nj < n:
            nk = ck - (1 if grid[ni][nj] == 'T' else 0)
            
            if nk >= 0 and not visited[ni][nj][d][nk]:
                visited[ni][nj][d][nk] = True
                queue.append((ni, nj, d, nk, cnt + 1))
        
        for nd in [(d + 3) % 4, (d + 1) % 4]:
            if visited[ci][cj][nd][ck]: continue

            visited[ci][cj][nd][ck] = True
            queue.append((ci, cj, nd, ck, cnt + 1))
    
    return -1            

if __name__ == "__main__":
    for tc in range(int(input())):
        print(f'#{tc + 1} {solve()}')