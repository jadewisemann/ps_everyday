def search(left, right, target):
    counter = 0
    while left <= right:
        counter += 1
        mid = (left + right) // 2
        if mid == target:
            break
        elif mid > target:
            right = mid
        elif mid < target:
            left = mid
    return counter

for tc in range(int(input())):
    p, a, b = map(int, input().split())
    
    counter_a = search(1, p, a)
    counter_b = search(1, p, b)
    
    winner  = ( 
        "A" if counter_a < counter_b
        else "B" if counter_b < counter_a
        else 0 
    )
    
    print(f'#{tc + 1} {winner}')
