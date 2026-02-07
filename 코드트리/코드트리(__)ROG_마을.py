from collections  import deque

ip = lambda: map(int, input().split())

n, a = ip()
grp = [list(ip()) for _ in range(n)]
xi, yi = ip()
xj, yj = ip()
xi, yi, xj, yj = xi-1, yi-1, xj-1, yj-1
# 012 = ROG

que = deque([(xi, yi, 0)])
vis = set([(xi, yi, 0)])
res = -1


while que:
    cx, cy, ct = que.popleft()

    if cx == xj and cy == yj:
        res = ct
        break

    nt = ct + 1

    for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = cx + dx, cy + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        color = grp[nx][ny]
        if color == 1:
            color = (1 + (nt // a)) % 3

        if (dx == 0 and dy ==  0) or color == 2:
            next = (nx, ny, nt % (3 * a))
            if next not in vis:
                vis.add(next)
                que.append((nx, ny, nt))

print(res)