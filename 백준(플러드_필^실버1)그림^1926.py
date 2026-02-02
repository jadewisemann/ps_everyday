ip  = lambda: map(int, input().split())

n, m = ip()
grp = [list(ip()) for _ in range(n)]

cnt = 0
glo_max = 0

def dfs(i, j):
    area = 0
    qu = set()
    qu.add((i, j))
    while qu:
        si, sj = qu.pop()
        area += 1
        grp[si][sj] = 0

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si + di, sj + dj
            
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if grp[ni][nj] == 1:
                qu.add((ni, nj))
    return area         

for i in range(n):
    for j in range(m):
        if grp[i][j] == 1:
            tmp = dfs(i, j)
            if tmp > glo_max:
                glo_max = tmp
            cnt += 1

print(cnt)
print(glo_max)