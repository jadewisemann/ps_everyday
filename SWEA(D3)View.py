for tc in range(1, 10 + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    rst = 0
    for i in range(2, n-2):
        bottom_height = max(arr[i-2],arr[i-1], arr[i+1], arr[i+2])
        view = arr[i] - bottom_height
        if view > 0:
            rst += view

    print(f'#{tc} {rst}')