 
# u -> r -> d -> l
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

for tc in range(int(input())):
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    
    si, sj, ei, ej = 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'X': si, sj = i, j
            if grid[i][j] == 'Y': ei, ej = i, j

    print(f'#{tc + 1}', end=' ')

    for _ in range(int(input())):
        ci, cj = si, sj
        d = 0
        _, query = input().split()
        for op in query:
            if op == 'R': d =  (d + 1) % 4
            elif op == 'L': d =  (d - 1) % 4
            elif op == 'A':
                di, dj = dirs[d]
                ni, nj = ci + di, cj + dj

                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] != 'T':
                    ci, cj = ni, nj
        print('1' if ci == ei and cj == ej else '0', end=' ')
    print()

