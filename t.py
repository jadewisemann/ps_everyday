ip = lambda: map(int, input().split())
for tc in range(int(input())):
    n, m = ip()
    arr = list(ip())
    sub_arr = list(ip())
    curr = 0
    for i in  range(n):
        if curr < m and arr[i] == sub_arr[curr]:
            curr += 1
            
    print(f'#{tc + 1} {"YES" if curr == m else "NO"}')


    