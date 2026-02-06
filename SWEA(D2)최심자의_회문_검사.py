for tc in range(int(input())):
    a = input().strip()
    print(f'#{tc + 1}', +(a == a[::-1]))