

def solve(n, m, grid, iceberg_count, si, sj):
    
    max_cells = n * m

    queue_i = [0] * max_cells
    queue_j = [0] * max_cells
    melt_i = [0] * max_cells
    melt_j = [0] * max_cells
    melt_amount = [0] * max_cells


    visited = [[0] * m for _ in range(n)]
    
    year = 0

    while iceberg_count > 0:
        year += 1

        queue_head = 0
        queue_tail = 0

        queue_i[queue_tail] = si
        queue_j[queue_tail] = sj
        queue_tail += 1
        visited[si][sj] = year

        melt_tail = 0

        while queue_head < queue_tail:
            ci = queue_i[queue_head]
            cj = queue_j[queue_head]
            queue_head += 1

            adj_sea_count = 0
            
            ni = ci - 1
            if grid[ni][cj] == 0:
                adj_sea_count += 1
            elif visited[ni][cj] != year:
                visited[ni][cj] = year
                queue_i[queue_tail] = ni
                queue_j[queue_tail] = cj
                queue_tail += 1
                
            ni = ci + 1
            if grid[ni][cj] == 0:
                adj_sea_count += 1
            elif visited[ni][cj] != year:
                visited[ni][cj] = year
                queue_i[queue_tail] = ni
                queue_j[queue_tail] = cj
                queue_tail += 1
                
            nj = cj - 1
            if grid[ci][nj] == 0:
                adj_sea_count += 1
            elif visited[ci][nj] != year:
                visited[ci][nj] = year
                queue_i[queue_tail] = ci
                queue_j[queue_tail] = nj
                queue_tail += 1
                
            nj = cj + 1
            if grid[ci][nj] == 0:
                adj_sea_count += 1
            elif visited[ci][nj] != year:
                visited[ci][nj] = year
                queue_i[queue_tail] = ci
                queue_j[queue_tail] = nj
                queue_tail += 1
            
            if adj_sea_count > 0:
                melt_i[melt_tail] = ci
                melt_j[melt_tail] = cj
                melt_amount[melt_tail] = adj_sea_count
                melt_tail += 1
            
        if queue_tail != iceberg_count:
            return year - 1
        
        for k in range(melt_tail):
            mi, mj = melt_i[k], melt_j[k]

            grid[mi][mj] -= melt_amount[k]

            if grid[mi][mj] <= 0:
                grid[mi][mj] = 0
                iceberg_count -= 1
        
        if iceberg_count > 0:
            for k in range(queue_tail - 1, -1, -1):
                if grid[queue_i[k]][queue_j[k]] > 0:
                    si, sj = queue_i[k], queue_j[k]
                    break
    
    return 0

def main():

    input_data = open(0).read().split()

    n = int(input_data[0])
    m = int(input_data[1])
    
    raw_data = list(map(int, input_data[2:]))

    grid = [
        raw_data[i * m : (i + 1) * m]
        for i in range(n)
    ]

    iceberg_count = 0
    si, sj = 0, 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] > 0:
                iceberg_count += 1
                si, sj = i, j

    ans = solve(n, m, grid, iceberg_count, si, sj)
    print(ans)

if __name__ == "__main__":
    main()
    
    