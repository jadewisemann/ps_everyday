def solve():
    n, m, h = map(int, input().split())

    board = [
        [False] * (n + 1)
        for _ in range(h + 1)
    ]
    
    for _ in range(m):
        a, b = map(int, input().split())
        board[a][b] = True

    def is_valid():
        for start in range(1, n + 1):
            curr = start
            for r in range(1, h + 1):
                if board[r][curr]:       curr += 1
                elif board[r][curr - 1]: curr -= 1

            if curr != start: return False
        return True

    candidates = [
        (i, j)
        for i in range(1, h + 1) 
        for j in range(1, n)
        if not (
            board[i][j] and 
            board[i][j-1] and
            board[i][j+1]
        )
    ]

    def dfs(count, limit, index):
        odd_count = 0
        for j in range(1, n):
            col_sum = 0
            for i in range(1, h + 1):
                if board[i][j]: col_sum += 1
            if col_sum % 2 == 1:
                odd_count += 1
        
        if odd_count > limit - count: return False

        if count == limit: return is_valid()

        for k in range(index, len(candidates)):
            ci, cj = candidates[k]
            
            if board[ci][cj-1] or board[ci][cj+1]:
                continue
                
            board[ci][cj] = True
            if dfs(count + 1, limit, k + 1): return True
            board[ci][cj] = False
            
        return False

    for limit in range(4):
        if dfs(0, limit, 0):
            print(limit)
            return
    
    print(-1)

if __name__ == "__main__":
    solve()