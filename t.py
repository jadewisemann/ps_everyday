for _ in range(10):
    tc=int(input().strip())
    arr=[list(map(int, input().split())) for _ in range(100)]
    cnt=0

    # 대각선
    total_diag1, total_diag2 = 0, 0
    for r in range(100):
        total_diag1 +=arr[r][r]
        total_diag2 +=arr[r][99-r]
        cnt = max(cnt, total_diag1, total_diag2)
        
        # 행 열
        total_col, total_row = 0, 0
        for c in range(100): 
            total_col +=arr[r][c]
            total_row +=arr[c][r]
            cnt = max(cnt, total_col,total_row)

    print(f'#{tc} {cnt}')