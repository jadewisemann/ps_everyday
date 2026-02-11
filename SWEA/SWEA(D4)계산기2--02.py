for tc in range(10):
    input()
    
    total = 0
    for elem in input().split('+'):
        res = 1
        for num in elem.split('*'):
            res *= int(num)

        total += res 
        
    print(f'#{tc} {total}')