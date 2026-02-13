from collections import deque

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    pizzas = deque([i + 1, v] for i, v in enumerate(map(int, input().split())))
    oven = deque(pizzas.popleft() for _ in range(n))
    
    while len(oven) > 1:
        pizza = oven.popleft()  
        pizza[1] //= 2          
        
        if pizza[1] > 0:        
            oven.append(pizza)
        
        elif pizzas:       
            oven.append(pizzas.popleft())
            
    print(f'#{tc} {oven[0][0]}')