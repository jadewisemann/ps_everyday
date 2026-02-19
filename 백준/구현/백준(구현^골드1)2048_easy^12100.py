MAX_COUNT = 5

def merge(temp):
    n = len(temp)
    temp = [x for x in temp if x]

    new_line = []
    
    i = 0
    while i < len(temp):
        if i + 1 < len(temp) and temp[i] == temp[i+1]:
            new_line.append(temp[i] * 2)
            i += 2
        else:
            new_line.append(temp[i])
            i += 1
    
    return new_line + [0] * (n - len(new_line))

def dfs(count, board, curr_best):
    local_max = max(map(max, board))
    curr_best = max(curr_best, local_max)

    if local_max * (2 ** (MAX_COUNT - count)) <= curr_best:
        return curr_best
    
    if count == MAX_COUNT:
        return curr_best
    
    for _ in range(4):
        moved_board = [merge(row) for row in board]
        if moved_board != board:
            curr_best = dfs(count + 1, moved_board, curr_best)
        
        board = [list(x) for x in zip(*board[::-1])]

    return curr_best

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(dfs(0, board, 0))