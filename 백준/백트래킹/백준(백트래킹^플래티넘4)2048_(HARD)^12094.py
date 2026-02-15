MAX_COUNT = 10


def merge(line):
    n = len(line)
    line = [x for x in line if x]

    new_line = []
    
    i = 0
    while i < len(line):
        if i + 1 < len(line) and line[i] == line[i+1]:
            new_line.append(line[i] * 2)
            i += 2
        else:
            new_line.append(line[i])
            i += 1
            
    return new_line + [0] * (n - len(new_line))

def dfs(count, board, curr_best):
    local_max = max(map(max, board))

    if local_max * (2 ** (MAX_COUNT - count)) <= curr_best:
        return curr_best
    
    if count == MAX_COUNT:
        return max(local_max, curr_best)
    
    for _ in range(4):
        moved_board = [merge(row) for row in board]

        if moved_board != board:
            curr_best = dfs(count + 1, moved_board, curr_best)

        board = [list(x) for x in zip(*board[::-1])]

    return curr_best

import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

print(dfs(0, board, 0))