for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for _ in range(m):
        i, j = map(int, input().split())
        arr[i - 1: i - 1 + j] = [arr[i - 1]] * len(arr[i - 1: i -1 + j])
        
    print(f'#{tc + 1}', *arr)