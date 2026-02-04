for tc in range(int(input())):
    vis = [[0 for _ in range(10 + 1)] for _ in range(10 + 1)]
     
    n = int(input())
    reds =  set()
    blues = set()
 
    for _ in range(n):
        sx, sy, ex, ey, clr = map(int, input().split())
 
        for nx in range(sx, ex + 1):
            for ny in range(sy, ey + 1):
                if clr == 1:
                    reds.add((nx, ny))
                else:
                    blues.add((nx, ny))
       
    print(f'#{tc + 1} {len(reds & blues)}')