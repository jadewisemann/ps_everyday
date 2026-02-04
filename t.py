for _ in range(10):
    tc = int(input())
    grp = [list(map(int, input().split())) for _ in range(100)]

    max_val = 0

    diag1, diag2 = 0, 0
    for i in range(100):
        row_sum, col_sum = 0, 0
        for j in range(100):
            row_sum += grp[i][j]
            col_sum += grp[j][i]

            if i == j: 
                diag1 += grp[i][j]
            if i + j == 99:
                diag2 += grp[i][j]

        max_val = max(max_val, row_sum, col_sum)

    max_val = max(max_val, diag1, diag2)

    print(f'#{tc} {max_val}')



