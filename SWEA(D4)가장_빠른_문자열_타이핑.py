for tc in range(int(input())):
    a, b = input().split()
    print(f'#{tc + 1} {len(a.replace(b, "*"))}')