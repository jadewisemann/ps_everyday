for tc in range(int(input())):
    n = int(input())
    
    max_val, min_val = 0, float('inf')

    for el in list(map(int, input().split())):
        if el > max_val: 
            max_val = el
        if el < min_val:
            min_val = el
    
    print(f'#{tc+1} {max_val - min_val}')
        