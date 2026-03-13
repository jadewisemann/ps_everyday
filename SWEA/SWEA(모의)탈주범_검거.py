from collections import deque
 
STRUCTURE = [
    (),
    {(0, 1), (1, 0), (0, -1), (-1, 0)},
    {(1, 0), (-1, 0)},
    {(0, 1), (0, -1)},
    {(-1, 0), (0, 1)},
    {(1, 0), (0, 1)},
    {(0, -1), (1, 0)},
    {(-1, 0), (0, -1)},
]

# dirs: 상1 하2 좌4 우8
STRUCTURE_BITMASK = (0, 15, 3, 12, 9, 10, 6, 5)
 
MOVES = (
    (-1,  0,  1,  2),
    ( 1,  0,  2,  1), 
    ( 0, -1,  4,  8),
    ( 0,  1,  8,  4)  
)

VALID_MOVES = (
    (),
    ((-1, 0, 2), (1, 0, 1), (0, -1, 8), (0, 1, 4)), 
    ((-1, 0, 2), (1, 0, 1)),                        
    ((0, -1, 8), (0, 1, 4)),                        
    ((-1, 0, 2), (0, 1, 4)),                        
    ((1, 0, 1), (0, 1, 4)),                         
    ((1, 0, 1), (0, -1, 8)),                        
    ((-1, 0, 2), (0, -1, 8))                        
)


def get_input():
    n, m, r, c, l = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ] # grid[i...n][j...m]
 
    return n, m, r, c, l, grid
 

def get_input_padded():
    n, m, r, c, l = map(int, input().split())
    
    grid = [[0] * (m + 2)]
    for _ in range(n):
        grid.append([0] + list(map(int, input().split())) + [0])
    grid.append([0] * (m + 2))
    
    return n, m, r + 1, c + 1, l, grid

 
def solve():
    st = STRUCTURE
 
    n, m, r, c, l = map(int, input().split())
 
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ] # grid[i...n][j...m]
 
    vis = [[False] * m for _ in range(n)]
    vis[r][c] = True
 
    q = deque([(r, c, 1)])
    count = 1
 
    while q:
        ci, cj, time = q.popleft()
        if time >= l: continue
 
        for di, dj in st[grid[ci][cj]]:
            ni, nj = ci + di, cj + dj
            if (
                not(0 <= ni < n and 0 <= nj < m) or
                not grid[ni][nj] or
                vis[ni][nj]
            ): continue
            if (-di, -dj) in st[grid[ni][nj]]:
                vis[ni][nj] =True
                q.append((ni, nj, time + 1))
                count += 1
 
    return count 
 
 
def solve_level_order():
    st = STRUCTURE
     
    n, m, r, c, l, grid = get_input()
 
    vis = [[False] * m for _ in range(n)]
    vis[r][c] = True
 
    curr_q = [(r, c)]
    count = 1
     
    for _ in range(l - 1):
        if not curr_q: break
 
        nxt_q = []
        for ci, cj in curr_q:
            for di, dj in st[grid[ci][cj]]:
                ni, nj = ci + di, cj + dj
                if (
                    not(0 <= ni < n and 0 <= nj < m) or
                    not grid[ni][nj] or
                    vis[ni][nj]
                ): continue
                if (-di, -dj) in st[grid[ni][nj]]:
                    vis[ni][nj] =True
                    nxt_q.append((ni, nj))
                    count += 1
 
        curr_q = nxt_q
    return count


def solve_bitmask():
    structures = STRUCTURE_BITMASK
    moves = MOVES
 
    n, m, r, c, l, grid = get_input()
     
    vis = [[False] * m for _ in range(n)]
    vis[r][c] = True
 
    max_size = n * m
    q_r = [0] * max_size
    q_c = [0] * max_size
    q_time = [0] * max_size
    head = tail = 0
 
    q_r[tail] = r
    q_c[tail] = c
    q_time[tail] = 1
    tail += 1
 
    while head < tail:
        ci = q_r[head]
        cj = q_c[head]
        time = q_time[head]
        head += 1
 
        if time >= l: continue
 
        curr = structures[grid[ci][cj]]
 
        for di, dj, my_bit, opp_bit in moves:
            if curr & my_bit:
                ni, nj = ci + di, cj + dj
 
                if not (0 <= ni < n and 0 <= nj < m): continue
                if vis[ni][nj]: continue
                 
                if structures[grid[ni][nj]] & opp_bit:
                    vis[ni][nj] = True
 
                    q_r[tail] = ni
                    q_c[tail] = nj
                    q_time[tail] = time + 1
                    tail += 1
 
    return tail
 


def solve_bitmask_optimize():
    structures = STRUCTURE_BITMASK
    valid_moves = VALID_MOVES

    n, m, r, c, l, grid = get_input_padded()
    
    vis = [[False] * (m + 2) for _ in range(n + 2)]
    vis[r][c] = True

    max_size = n * m
    q_r = [0] * max_size
    q_c = [0] * max_size
    q_time = [0] * max_size
    head = tail = 0

    q_r[tail] = r
    q_c[tail] = c
    q_time[tail] = 1
    tail += 1

    while head < tail:
        ci = q_r[head]
        cj = q_c[head]
        time = q_time[head]
        head += 1

        if time >= l: break

        for di, dj, opp_bit in valid_moves[grid[ci][cj]]:
            ni, nj = ci + di, cj + dj

            if vis[ni][nj]: continue
            
            if structures[grid[ni][nj]] & opp_bit:
                vis[ni][nj] = True

                q_r[tail] = ni
                q_c[tail] = nj
                q_time[tail] = time + 1
                tail += 1

    return tail

def main():
    for tc in range(int(input())):
        ans = solve_bitmask_optimize()
        print(f'#{tc + 1} {ans}')

if __name__ == "__main__":
    main()