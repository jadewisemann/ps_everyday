from collections import deque
from itertools import combinations

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    sx, sy = x, y
    ex, ey = x, y
    queue = deque([(x, y)])
    arr[x][y] += 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] += 1
                queue.append((nx, ny))
                ex, ey = max(nx, ex), max(ny, ey)
    return (sx, sy), (ex, ey)

def connect(islands):
    for i, j in combinations(range(len(islands)), 2):
        start1, end1 = islands[i]
        sx1, sy1 = start1
        ex1, ey1 = end1
        start2, end2 = islands[j]
        sx2, sy2 = start2
        ex2, ey2 = end2

        dist = 0
        x1, x2 = set(range(sx1, ex1+1)), set(range(sx2, ex2+1))
        if x1.intersection(x2):
            dist = min(abs(sy1-sy2), abs(sy1-ey2), abs(ey1-sy2), abs(ey1-ey2)) - 1
        else:
            y1, y2 = set(range(sy1, ey1+1)), set(range(sy2, ey2+1))
            if y1.intersection(y2):
                dist = min(abs(sx1-sx2), abs(sx1-ex2), abs(ex1-sx2), abs(ex1-ex2)) - 1

        if dist:
            lst.append((dist, i, j))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    islands = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                islands.append(bfs(i, j))

    lst = []
    connect(islands)
    lst.sort(key=lambda x: x[0])

    parent = [i for i in range(len(islands))]
    cost, connected = 0, 0
    for dist, i, j in lst:
        if connected == len(islands) - 1:
            break
        pi, pj = find(i), find(j)
        if pi != pj:
            parent[pi] = pj
            cost += dist
            connected += 1
    if connected == len(islands) - 1:
        print(f'#{tc}', cost)
    else:
        print(f'#{tc}', -1)