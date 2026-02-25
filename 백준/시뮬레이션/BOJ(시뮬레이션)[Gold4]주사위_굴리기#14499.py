n, m, x, y, k = map(int, input().split())
# grid[i < n][j < m]
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 0, 위, 뒤, 오, 왼, 앞, 아래
dice = [0] * 7

# 1동 > 2서 < 3북 /\ 4남 \/
command = list(map(int, input().split()))

rotate_map = {
    1: (4, 2, 1, 6, 5, 3), # 동
    2: (3, 2, 6, 1, 5, 4), # 서
    3: (5, 1, 3, 4, 6, 2), # 북
    4: (2, 6, 3, 4, 1, 5)  # 남
}

dirs = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]

ci, cj = x, y

for comm in command:
    ni, nj = ci + dirs[comm][0], cj + dirs[comm][1]
    if not (0 <= ni < n and 0 <= nj < m): continue

    dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = [dice[i] for i in rotate_map[comm]]

    if grid[ni][nj] == 0:
        grid[ni][nj] = dice[6]
    else:
        dice[6] = grid[ni][nj]
        grid[ni][nj] = 0

    ci, cj  = ni, nj
    print(dice[1])
