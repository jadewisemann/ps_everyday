
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    cabs = set()
    for _ in range(k):
        cabs.add(tuple(map(int, input().split())))

    count = 0


    while cabs:
        x, y = cabs.pop()
        count += 1

        stack = [(x,y)]
        while stack:
            sx, sy = stack.pop()

            for dx, dy in [[-1, 0], [1,0], [0, 1], [0, -1]]:
                nx, ny = sx + dx, sy + dy 
            
                if (nx, ny) in cabs:
                    cabs.remove((nx, ny))
                    stack.append((nx, ny))

                
    print(count)
                    


