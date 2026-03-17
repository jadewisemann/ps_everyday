n, m, h = map(int, input().split())

board = [[False] * (n + 1) for _ in range(h + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = True

def check():
    wrong_cnt = 0
    
    # 모든 사다리 확인
    for start_ladder in range(1, n + 1):
        # 시작점 저장
        curr_pos = start_ladder
        # 내려가면서 좌우로 움직이기
        for i in range(1, h + 1):
            if board[i][curr_pos]:        
                curr_pos += 1
            elif board[i][curr_pos - 1]:
                curr_pos -= 1
        
        # 다 내려갔는데 시작지점이랑 다르다 => 문제 있음
        if curr_pos != start_ladder:
            wrong_cnt += 1
    
    # 모든 사다리 중 틀린 위치 반환
    return wrong_cnt

min_val = 3 + 1

def dfs(curr_cnt, x, y):
    global min_val
    
    # 가지치기: 지금 까지 최소 갯수보다 많아버리면 안봄
    if curr_cnt >= min_val: return
    
    # 틀린 사다리 개수
    wrong_cnt = check()
    
    # 틀린 사다리가 없다? => 정답
    if wrong_cnt == 0:
        # 비교 없이 바로 갱신 => 위에서 걸렀음
        min_val = curr_cnt
        return
    
    # 가치지기: min_val - 1 - curr_cnt = 더 놓을 수 있는 가로선 개수
    # 만약에 그거 2배한 값보다 틀린게 많다? 절대 못고침
    # 하나의 가로선을 두면 두개가 바뀌기 때문에
    if wrong_cnt > (min_val - 1 - curr_cnt) * 2: return
        
    # 사다리 타고 내려가면서 확인하기
    # 지금 위치 보다 앞선 모든 사다리에 대해서 확인
    for i in range(x, h + 1):
        # 시작할 지점은 y
        start_y = y if i == x else 1
        
        for j in range(start_y, n):
            if board[i][j]:     continue
            if board[i][j - 1]: continue
            if board[i][j + 1]: continue
                
            board[i][j] = True
            dfs(curr_cnt + 1, i, j + 2)  
            board[i][j] = False

dfs(0, 1, 1)

print(min_val if min_val < 4 else -1)