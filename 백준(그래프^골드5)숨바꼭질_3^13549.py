from collections import deque

n, k = map(int, input().split())
dist = [-1] * (10**5 + 1)

dq = deque([n])
dist[n] = 0

while dq:
    curr = dq.popleft()

    if curr == k:
        print(dist[curr])
        break
    
    for next, time in [(curr * 2, 0), (curr - 1, 1), (curr + 1, 1)]:
        if 0 <= next <= 10**5 and dist[next] == -1:
            dist[next] = dist[curr] + time
            if time: 
                dq.append(next)
            else: 
                dq.appendleft(next)


