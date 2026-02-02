T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    curr = sum(arr[i] for i in range(m))
    rst = [curr]

    for idx in range(n - m):
        curr = curr - arr[idx] + arr[idx + m]
        rst.append(curr)

    print(f'#{tc+1} {max(rst) - min(rst)}')

