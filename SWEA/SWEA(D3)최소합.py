def get_input():
    n = int(input())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    return n, grid

def solve_dfs():
    n, grid = get_input()

    min_val = float('inf')
    
    def dfs(si, sj, curr_sum):
        nonlocal min_val
        
        if si == n - 1 and sj == n - 1:
            if curr_sum < min_val:
                min_val = curr_sum
                return 

        for di, dj in ((1, 0), (0, 1)):
            ni, nj = si + di, sj + dj
            if not(0 <= ni < n and 0 <= nj < n): continue
            dfs(ni, nj, curr_sum + grid[ni][nj])

    dfs(0, 0, grid[0][0])

    return min_val

def solve_dp():
    n, grid = get_input()

    for i in range(1, n):
        grid[i][0] +=  grid[i - 1][0]
        grid[0][i] +=  grid[0][i - 1]

    for i in range(1, n):
        for j in range(1, n):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[n - 1][n - 1]


def solve_space_optimize():
    n, grid = get_input()
    dp = [0] * n
    dp[0] = grid[0][0]

    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]

    for i in range(1, n):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

    return dp[n - 1] 


def main():
    for tc in range(int(input())):
        ans = solve_space_optimize()
        print(f'#{tc + 1} {ans}')

if __name__ == "__main__":
    main()