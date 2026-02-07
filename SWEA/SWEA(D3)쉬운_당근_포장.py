for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(arr)

    min_val = 999
    
    for i in range(n - 2):
        if sorted_arr[i] == sorted_arr[i+1]:
            continue
        for j in range(i + 1, n - 1):
            if sorted_arr[j] == sorted_arr[j+1]:
                continue
            
            s, m, l = i + 1, j - i, n - j - 1   
            if s <= 0 or m <= 0 or  l <= 0:
                continue
            
            gap = max(s, m, l) - min(s, m, l)
            if gap < min_val:
                min_val = gap
            
    
    print(f'#{tc + 1} {min_val if min_val != 999 else -1}')

