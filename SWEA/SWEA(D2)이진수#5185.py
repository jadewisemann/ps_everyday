for tc in range(int(input())):
    print(f'#{tc + 1} {"".join(f"{int(c, 16):04b}" for c in input().split()[1])}')