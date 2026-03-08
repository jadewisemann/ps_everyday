def get_direcitons(start_dir, generation):
    directions = [start_dir]
    for _ in range(generation):
        directions += [(d + 1) % 4 for d in directions[::-1]]
    return directions


def draw_curve(grid, j, i, directions):
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    
    grid[i][j] = True

    for d in directions:
        i += di[d]
        j += dj[d]
        grid[i][j] = True


def solve():
    n = int(input())

    grid = [[False] * 101 for _ in range(101)]
    for _ in range(n):
        x, y, d, g = map(int, input().split())    
        curve_dirs = get_direcitons(d, g)
        draw_curve(grid, x, y, curve_dirs)


    print(
        sum(
            grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]
            for i in range(100)
            for j in range(100)
        )
    )

if __name__ == "__main__":
    solve()