def solve(n, m, grid):
    '''상태트리 정의
    감시 타워의 방향에 의존?
    vis에 타워 치워넣어주고 계산하기
    '''
    vis = [
        [False for _ in range(n) ]
        for _ in range(m)
    ]

    passage_count = 0
    towers = [0] * (n * m)
    thead, ttail = 0, 0
    # 타워 추출
    for i in range(n):
        for j in range(m):
            curr = grid[i][j] 
            if curr == 0:
                passage_count += 1
            elif curr != 6:
                towers[ttail] = curr
                ttail += 1
    # 
    min_val = 8 * 8 + 1
    
    def backtrackig(curr_idx, curr_val, curr_dir):
        nonlocal min_val
        # base conditino
        if curr_idx == ttail - 1:
            if curr_val < min_val:
                curr_val = min_val
                return
                 
        # set visit
        

        # call backtracking

        # restore visit

        pass
    
    
        
    

    pass


def main():
    n, m = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ] # grid[i < n][j < m]x
    answer = solve(n, m, grid)
    print(answer)