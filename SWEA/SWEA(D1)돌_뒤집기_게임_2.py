I = lambda: map(int, input().split())

for tc in range(int(input())):
    n, m = I()
    arr = list(I())

    for _ in range(m):
        i, j = I()

        for curr in range(1, j + 1):
            nl, nr = i - 1 - curr, i - 1 + curr
            
            if nl < 0 or nr >= n:
                break

            if arr[nl] == arr[nr]:
                arr[nl], arr[nr] = 1 - arr[nl], 1 - arr[nr]
            
    print(f'#{tc + 1}', *arr)