for tc in range(int(input())):
    ax, ay, ap, aq = map(int, input().split())
    bx, by, bp, bq = map(int, input().split())
    
    if (
        ap < bx 
        or aq < by
        or bq < ax
        or bp < ay
    ): res = 4 
    
    elif (
        (ap, aq) == (bx, by)
        or (ax, aq) == (bp, by)
        or (ap, ay) == (bx, bq)
        or (ax, ay) == (bp, bq)
    ): res = 3

    elif (
        ap == bx
        or aq == by
        or ax == bp
        or ay == bq
    ): res = 2

    else: res = 1


    print(f'#{tc + 1} {res}')