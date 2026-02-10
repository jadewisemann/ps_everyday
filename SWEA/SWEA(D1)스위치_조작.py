
for tc in range(int(input())):
    _ = input()
    cnt = 0
    for p, t in zip(input().split(), input().split()):
        cnt += (int(p) ^ (cnt % 2)) != int(t)
        
    print(f'#{tc + 1} {cnt}')