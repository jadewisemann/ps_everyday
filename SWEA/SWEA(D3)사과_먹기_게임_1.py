def find_apple(n, grid):
    apples = [0] * (n * n + 1)
    max_apple = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                apples[grid[i][j]] = (i, j)
                if grid[i][j] > max_apple:
                    max_apple = grid[i][j]
    return apples, max_apple


def solve(n, grid):
    apples, max_apple = find_apple(n, grid)
    curr_i, curr_j, curr_d = 0, 0, 0
    total_rotations = 0

    for i in range(1, max_apple + 1):
        if apples[i] == 0: continue
        
        target_i, target_j = apples[i]

        dirs = []
        if target_i > curr_i: dirs.append(1)
        elif target_i < curr_i: dirs.append(3)
        
        if target_j > curr_j: dirs.append(0)
        elif target_j < curr_j: dirs.append(2)
        
        d1, d2 = dirs[0], dirs[-1]
        turns, curr_d =  min(
            ((d1 - curr_d) % 4 + (d2 - d1) % 4, d2),
            ((d2 - curr_d) % 4 + (d1 - d2) % 4, d1)
        )
        
        total_rotations += turns
        curr_i, curr_j = target_i, target_j

    return total_rotations

def get_input():
    n = int(input())
    grid = [
        list(map(int, input().split())) 
        for _ in range(n)
    ]

    return n, grid

def main():
    for tc in range(int(input())):
        n, grid = get_input()
        ans = solve(n, grid)
        print(f'#{tc + 1} {ans}')

if __name__ == "__main__":
    main()