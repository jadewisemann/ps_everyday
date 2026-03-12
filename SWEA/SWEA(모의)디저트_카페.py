di = [1,  1, -1, -1]
dj = [1, -1, -1,  1]

def solve():
    n  = int(input())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    res = - 1

    def dfs(i, j,  dist, dir):
        nonlocal si, sj, res
        if dir == 3 and i == si and j == sj:
            res = max(res, len(visited))
            return
        
        for d in range(dir, dir + 2):
            if d > 3: break

            ni, nj = i + di[d], j + dj[d]
            
            if not(0 <= ni < n and 0 <= nj < n): continue
            
            if grid[ni][nj] not in visited:
                visited.append(grid[ni][nj])
                dfs(ni, nj, dist + 1, d)
                visited.pop()
            elif d == 3 and ni == si and nj == sj:
                dfs(ni, nj, dist + 1, d)
        
    for i in range(n):
        for j in range(n):
            si, sj = i, j
            visited = [grid[i][j]]
            dfs(i, j, 1, 0)
    return res
        


def main():
    for tc in range(int(input())):
        ans = solve()
        print(f'#{tc + 1} {ans}')

if __name__ == "__main__":
    main()