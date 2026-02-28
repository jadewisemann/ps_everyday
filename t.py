n, m = map(int, input().split())
# grid[i < n][j < m]
grid = [
    list(map(int, input()))
    for _ in range(n)
]

cnt = 0
while True:
    # 빙산 찾기
    delegation_iceberg = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                tmp = grid[i][j]
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj]: continue
                        tmp -= 1
                if tmp <= 0:
                    delegation_iceberg.add((i, j))
                else:
                    grid[i][j] = tmp
    
    for i, j in delegation_iceberg:
        grid[i][j] = 0
    
    # 분리 확인
    vis = []

print(cnt)
