T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc + 1} {max(arr) - min(arr)}') 