def solve():
    n = int(input())
    board = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    cores = [
        (i, j)
        for i in range(1, n-1)
        for j in range(1, n-1)
        if board[i][j] == 1
    ]

    max_cores = 0
    min_wires = float('inf')
    num_cores = len(cores)

    def fill(i, j, di, dj, val):
        cnt = 0
        ni, nj = i + di, j + dj
        while 0 <= ni < n and 0 <= nj < n:
            board[ni][nj] = val
            ni += di
            nj += dj
            cnt += 1
        return cnt

    def can_proceed(i, j, di, dj):
        ni, nj = i + di, j + dj
        while 0 <= ni < n and 0 <= nj < n:
            if board[ni][nj] != 0:
                return False
            ni += di
            nj += dj
        return True

    def dfs(curr_idx, core_cnt, wire_cnt):
        nonlocal max_cores, min_wires

        if curr_idx == num_cores:
            if core_cnt > max_cores:
                max_cores, min_wires = core_cnt, wire_cnt
            elif core_cnt == max_cores:
                min_wires = min(min_wires, wire_cnt)
            return

        if (num_cores - curr_idx) + core_cnt < max_cores:
            return

        i, j = cores[curr_idx]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if can_proceed(i, j, di, dj):
                dist = fill(i, j, di, dj, 2)
                dfs(curr_idx + 1, core_cnt + 1, wire_cnt + dist)
                fill(i, j, di, dj, 0)

        dfs(curr_idx + 1, core_cnt, wire_cnt)

    dfs(0, 0, 0)
    return min_wires

for tc in range(int(input())):
    print(f"#{tc + 1} {solve()}")