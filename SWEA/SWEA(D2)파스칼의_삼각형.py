for tc in range(int(input())):
    row = [1]
    print(f'#{tc + 1}')
    for _ in range(int(input())):
        print(*row)
        row = [l + r for l, r in zip([0] + row, row + [0])]


