for tc in range(1, int(input()) + 1):
    n = int(input())

    matrix = [[0] * n for _ in range(n)]
    xy, dirs = 0 + 0j, 1 + 0j
    
    for i in range(1, n*n + 1):
        matrix[int(xy.imag)][int(xy.real)] = i
        
        nxy = xy + dirs
        nx, ny = int((nxy).imag), int((nxy).real)

        if not (0 <= nx < n and 0 <= ny < n) or matrix[nx][ny]:
            dirs *= 1j
        
        xy += dirs

    print(f'#{tc}')
    for row in matrix:
        print(*row)