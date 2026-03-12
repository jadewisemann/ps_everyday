def solve():
    n = int(input())

    board = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    
    cores = [
        (i, j)
        for i in range(1, n - 1)
        for j in range(1, n - 1) 
        if board[i][j] == 1 
    ]
    
    num_cores = len(cores)

    max_cores = 0
    min_wire = float('inf')

    def dfs(curr_idx, core_cnt, wire_cnt):
        nonlocal max_cores, min_wire
        
        if core_cnt + (num_cores - curr_idx) < max_cores:
            return

        if curr_idx == num_cores:
            if core_cnt > max_cores:
                max_cores = core_cnt
                min_wire = wire_cnt
            elif core_cnt == max_cores:
                min_wire = min(min_wire, wire_cnt)
            return

        ci, cj = cores[curr_idx]

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            path = []
            ni, nj = ci + di, cj + dj
            can_connect = True

            while 0 <= ni < n and 0 <= nj < n:
                if board[ni][nj] != 0:
                    can_connect = False
                    break

                path.append((ni, nj))
                ni += di
                nj += dj
            
            if can_connect:
                for pi, pj in path:
                    board[pi][pj] = 2

                dfs(curr_idx + 1, core_cnt + 1, wire_cnt + len(path))
                
                for pi, pj in path:
                    board[pi][pj] = 0
            
        dfs(curr_idx + 1, core_cnt, wire_cnt)

    dfs(0, 0, 0)
    return min_wire

def main():
    for tc in range(int(input())):
        min_wire = solve()
        print(f"#{tc + 1} {min_wire}")

if __name__ == "__main__":
    main()