from collections import deque

n, k = map(int, input().split())

vis = [-1] * (10**5 + 1)


q = deque([(n, 0)])
vis[n] = 0
res = 0
min_len = -1

while q:
    curr, cnt = q.popleft()

    if curr == k:
        if min_len == -1:
            min_len = vis[curr]
            res = 1
        elif vis[curr] == min_len:
            res += 1
        continue

    for n_curr in (curr - 1, curr + 1, curr *    2):
        
        if not (0 <= n_curr <= 10**5): continue
        if vis[n_curr] == -1 or vis[n_curr] == vis[curr] + 1:            
            vis[n_curr] = vis[curr] + 1
            q.append((n_curr, cnt + 1))

print(min_len)
print(res)
