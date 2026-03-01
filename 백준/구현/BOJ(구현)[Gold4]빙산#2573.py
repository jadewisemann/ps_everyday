import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

icebergs = {
    (i, j)
    for i in range(n)
    for j in range(m)
    if grid[i][j]    
}

cnt = 0
while True:
    if not icebergs:
        cnt = 0
        break
  
    start_iceberg = next(iter(icebergs))
    stack = [start_iceberg]
    vis = {start_iceberg}

    while stack:
        ci, cj = stack.pop()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            
            if (ni, nj) not in icebergs: continue
            if (ni, nj) in vis: continue

            vis.add((ni, nj))
            stack.append((ni, nj))
    
    if len(vis) != len(icebergs):
        break 

    melting_amount = []
    for ci, cj in icebergs:
        sea_count = 0
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < n and 0 <= nj < m): continue
            if grid[ni][nj]: continue
            sea_count += 1
        if sea_count > 0:
            melting_amount.append((ci, cj, sea_count))

    for ci, cj, amount in melting_amount:
        if grid[ci][cj] <= amount:
            grid[ci][cj] = 0
            icebergs.remove((ci, cj))
        else: 
            grid[ci][cj] -= amount
    
    
    cnt += 1

print(cnt)