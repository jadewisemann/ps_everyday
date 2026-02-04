for tc in range(int(input())):
    vis = [[[False, False] for _ in range(10 + 1)] for _ in range(10 + 1)]
     
    n = int(input())
    for _ in range(n):
        sx, sy, ex, ey, clr = map(int, input().split())
  
        for nx in range(sx, ex + 1):
            for ny in range(sy, ey + 1):
                vis[nx][ny][clr-1] = True
  
    tmp = 0
    for row in vis:
        for r, b in row:
            if r and b:
                tmp += 1
      
    # tmp = sum(r and b for row in vis for r, b in row)
      
    print(f'#{tc + 1} {tmp}')