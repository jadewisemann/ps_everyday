from collections import deque

n, k = map(int, input().split())

dq = deque([(n, 0)])
vis = set()

while dq:
    curr, time = dq.popleft()
    # vis.add(new_curr)

    if curr == k:
        print(time)
        break

    for new_curr in [curr - 1, curr + 1, curr * 2]:
        if 0 <= new_curr <= 10**5 and new_curr not in vis:
            dq.append((new_curr, time + 1))
            vis.add(new_curr)



    
   