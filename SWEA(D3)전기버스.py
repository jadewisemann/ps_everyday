for tc in range(1, int(input()) + 1):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    curr = 0
    cnt = 0

    while curr + k < n:
        f = False

        for step in range(k, 0, -1):
            pos = curr + step
            if pos in arr:
                curr = pos
                cnt += 1
                f = True
                break
        
        if not f:
            cnt = 0
            break

    print(f'#{tc} {cnt}')