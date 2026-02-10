for tc in range(int(input())):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    min_n = min(n, m)
    rst = []
    for idx in range(min_n):
        rst.append(arr1[idx])
        rst.append(arr2[idx])
    rst += arr2[min_n:] if m > n else arr1[min_n:]
    print(f'#{tc + 1}', end=" ")
    print(*rst)