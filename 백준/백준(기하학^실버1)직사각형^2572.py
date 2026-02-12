for _ in range(4):
    ax, ay, ap, aq, bx, by, bp, bq = map(int, input().split())

    w = min(ap, bp) - max(ax, bx)
    h = min(aq, bq) - max(ay, by)

    print(
        'd' if w < 0 or h < 0 else
        'c' if w == 0 and h == 0 else 
        'b' if  w * h == 0 else
        'a'   
    )