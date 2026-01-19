def solve_compact(C, R, K):
    if K > C * R: return 0

    min_x, max_x = 1, C
    min_y, max_y = 1, R
    
    curr = 1
    step = 0

    while min_x <= max_x and min_y <= max_y:
        mode = step % 4        
        length = (max_y - min_y + 1) if mode % 2 == 0 else (max_x - min_x + 1)

        if K < curr + length:
            offset = K - curr
            if mode == 0:   return min_x, min_y + offset      
            elif mode == 1: return min_x + offset, max_y      
            elif mode == 2: return max_x, max_y - offset      
            elif mode == 3: return max_x - offset, min_y      

        curr += length
        if mode == 0:   min_x += 1   
        elif mode == 1: max_y -= 1   
        elif mode == 2: max_x -= 1   
        elif mode == 3: min_y += 1   
        
        step += 1

    return 0

C, R = map(int, input().split())
K = int(input())

result = solve_compact(C, R, K)
if result == 0:
    print(0)
else:
    print(f"{result[0]} {result[1]}")