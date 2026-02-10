for tc in range(int(input())):
    ax, ay, ap, aq = map(int, input().split())
    bx, by, bp, bq = map(int, input().split())

    w = min(ap, bp) - max(ax, bx)
    h = min(aq, bq) - max(ay, by)

    print(f'#{tc + 1}',(
        4 if w < 0 or h < 0 else
        3 if w == 0 and h == 0 else 
        2 if  w * h == 0 else
        1    
    ))