n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

command = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# start
clouds = [(n-1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

mapper = {
    1 : ( 0, -1), 
    2 : (-1, -1), 
    3 : (-1,  0), 
    4 : (-1,  1), 
    5 : ( 0,  1), 
    6 : ( 1,  1), 
    7 : ( 1,  0), 
    8 : ( 1, -1), 
}

for direction, dist in command:
    # move cloud + rain there
    new_clouds = []
    cloud_pos = [[False] * n for _ in range(n)]
    
    for si, sj in clouds:
        ni = (si + mapper[direction][0] * dist) % n
        nj = (sj + mapper[direction][1] * dist) % n
        grid[ni][nj] += 1
        new_clouds.append((ni, nj))
        cloud_pos[ni][nj] = True

    # copy water
    for si, sj in new_clouds:
        cnt = 0
        for di, dj in ((-1, -1), (-1, 1), (1, 1), (1, -1)):
            ni, nj = si + di, sj + dj
            if (0 <= ni < n and 0 <= nj < n) and grid[ni][nj] > 0: 
                cnt += 1
        grid[si][sj] += cnt
    
    # make cloud
    next_clouds = []
    for i in range(n):
        for j in range(n):
            if cloud_pos[i][j]: 
                continue
            if grid[i][j] >= 2:
                next_clouds.append((i, j))
                grid[i][j] -= 2
    
    clouds = next_clouds

print(sum(sum(row) for row in grid))