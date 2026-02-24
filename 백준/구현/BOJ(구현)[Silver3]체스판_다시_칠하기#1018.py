n, m = map(int, input().split())
board = [input() for _ in range(n)]
ans = 64

for i in range(n - 7):
    for j in range(m - 7):
        draw = sum(
            (board[r][c] == 'W') != ((r + c) % 2 == 0) 
            for r in range(i, i + 8)
            for c in range(j, j + 8)
        )
        
        ans = min(ans, draw, 64 - draw)

print(ans)