def solution():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    drc = ((0, 1), (0, -1), (1, 0), (-1, 0))

    max_val_possible = max(max(row) for row in arr)
    
    def dfs(i, r, c, w, global_max):
        if w + (4 - i) * max_val_possible <= global_max:
            return global_max

        if i == 4:
            return max(global_max, w)

        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc]:
                tmp = arr[nr][nc]
                
                arr[nr][nc] = 0
                
                if i == 2:
                    global_max = dfs(i + 1, r, c, w + tmp, global_max)
                
                global_max = dfs(i + 1, nr, nc, w + tmp, global_max)
                
                arr[nr][nc] = tmp
                
        return global_max

    ans = 0
    for i in range(n):
        for j in range(m):
            v = arr[i][j]
            arr[i][j] = 0
            ans = dfs(1, i, j, v, ans)
            arr[i][j] = v
            
    print(ans)

solution()