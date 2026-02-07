from collections import deque

n, m = map(int, input().split())
grp = [list(input().strip()) for _ in range(n)]


bx, by, rx, ry  = 0, 0, 0, 0
hx, hy = 0, 0
for idx, row in enumerate(grp):
    for jdx, el in enumerate(row):
        if el == "B":
            bx, by = idx, jdx
        
        elif el == "R":
            rx, ry = idx, jdx

def move(x, y, dx, dy):
    cnt = 0
    while grp[x + dx][y + dy] != "#" and grp[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def solve():
    dq = deque([(rx, ry, bx, by, 1)])
    vis = set([(rx, ry, bx, by)])

    while dq:
        
        crx, cry, cbx, cby, dist = dq.popleft()
        
        # 거리 제한
        if dist > 10:
            break


        # 순회
        for dx, dy in [(-1,  0), ( 1,  0), ( 0,  1), ( 0, -1)]:
            nrx, nry, rcnt = move(crx, cry, dx, dy)
            nbx, nby, bcnt = move(cbx, cby, dx, dy)

            # 파란 구슬 = 실패
            if grp[nbx][nby] == "O": continue

            # 빨강 구슬 = 성공
            if grp[nrx][nry] == "O":
                return dist
            
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            
            if (nrx, nry, nbx, nby) not in vis:
                vis.add((nrx, nry, nbx, nby))
                dq.append((nrx, nry, nbx, nby, dist + 1))

    return -1
ㅓ
print(solve())