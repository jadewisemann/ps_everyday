def get_data():
    n, m, h = map(int, input().split()) # n: 세로선, m: 가로선, h: 가로선을 놓을수 있는 위치

    board = [[False] * (n + 1) for _ in range(h + 1) ]

    for _ in range(m):
        a, b = map(int, input().split())
        board[a][b] = True

    return n, h, board

def check(n, h, board):
    for start in range(1, n + 1):
        curr = start
        for h in range(1, h + 1):
            if board[h][curr]:
                curr += 1
            elif board[h] [curr - 1]:
                curr -= 1
        if curr != start: return False
    
    return True

def dfs(n, h, board, limit, curr_cnt, x, y):
    global answer

    if check(n, h, board):
        ans = curr_cnt 
        return True
    
    if curr_cnt == limit: return False

    for i in range(x, h + 1):
        start_j = y if i == x else 1
        for j in range(start_j, n):
            if not board[i][j] and not board[i][j - 1] and not board[i][j + 1]:
                board[i][j] = True
                if dfs(n, h, board, limit, curr_cnt + 1, i, j + 2):
                    return True
                board[i][j] = False
    
    return False


def main():
    n, h, board = get_data()
    ans = -1

    for limit in range(4):
        if dfs(n, h, board, limit, 0, 1, 1):
            ans = limit
            break
        
    print(ans)


if __name__ == "__main__":
    main()