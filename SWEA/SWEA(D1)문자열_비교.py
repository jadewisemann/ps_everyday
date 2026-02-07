for tc in range(1, int(input()) + 1):
    a, b  = input(), input()
    print(f'#{tc} {1 if (a in b) else 0}')