def solve(n, m, grid, cctvs):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    cctv_modes = [
        [], 
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]], 
        [[0, 1], [1, 2], [2, 3], [3, 0]], 
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 
        [[0, 1, 2, 3]]
    ]

    def fill(i, j, directions, delta):
        covered = 0
        for d in directions:
            ni, nj = i, j
            while (
                0 <= (ni := ni + di[d]) < n 
                and 0 <= (nj := nj + dj[d]) < m 
                and grid[ni][nj] != 6
            ):
                if grid[ni][nj] == 0: covered += 1
                if grid[ni][nj] <= 0: grid[ni][nj] += delta
        return covered

    ans = sum(row.count(0) for row in grid)

    def backtrack(idx, current_empty):
        nonlocal ans
        if idx == len(cctvs):
            ans = min(ans, current_empty)
            return
        
        ci, cj, t = cctvs[idx]
        for dirs in cctv_modes[t]:
            watched = fill(ci, cj, dirs, -1)
            backtrack(idx + 1, current_empty - watched)
            fill(ci, cj, dirs, 1)

    backtrack(0, ans)
    return ans

def main():
    n, m = map(int, input().split())
    
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    cctvs = [
        (i, j, grid[i][j])
        for i in range(n)
        for j in range(m) 
        if 1 <= grid[i][j] <= 5
    ]

    ans = solve(n, m, grid, cctvs)
    print(ans)


if __name__ == '__main__':
    main()
