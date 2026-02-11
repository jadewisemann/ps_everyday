for tc in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for r in range(n):
        for c in range(n):
            si, sj, cnt = r, c, 
            while True:
                candidates = []
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = si + di, sj + dj
                    if (
                        0 <= ni < n and 0 <= nj < n 
                        and grid[ni][nj] < grid[si][sj]
                    ):
                        candidates.append((grid[ni][nj], ni, nj))

                if not candidates:
                    break

                _, si, sj = min(candidates)
                cnt += 1

            if cnt > res:
                res = cnt

    print(f'#{tc + 1} {res}')