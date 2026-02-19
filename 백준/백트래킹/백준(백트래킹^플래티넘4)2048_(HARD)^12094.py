import sys

input = sys.stdin.readline
MAX_COUNT = 10

def solve():
    line = input().strip()
    if not line: return
    n = int(line)
    initial_board = tuple(tuple(map(int, input().split())) for _ in range(n))

    ans = [0]
    memo = {}

    for row in initial_board:
        for val in row:
            if val > ans[0]:
                ans[0] = val

    def dfs(count, board, curr_max):
        if curr_max * (2 ** (MAX_COUNT - count)) <= ans[0]:
            return

        if memo.get(board, -1) >= (MAX_COUNT - count):
            return
        memo[board] = MAX_COUNT - count

        if count == MAX_COUNT:
            return

        curr_board = board
        for _ in range(4):
            new_board = []
            is_changed = False
            max_in_move = 0
            
            for row in curr_board:
                temp = [x for x in row if x]
                merged = []
                idx = 0
                while idx < len(temp):
                    if idx + 1 < len(temp) and temp[idx] == temp[idx+1]:
                        val = temp[idx] * 2
                        merged.append(val)
                        if val > max_in_move: max_in_move = val
                        idx += 2
                    else:
                        val = temp[idx]
                        merged.append(val)
                        if val > max_in_move: max_in_move = val
                        idx += 1
                
                merged += [0] * (n - len(merged))
                t_row = tuple(merged)
                new_board.append(t_row)
                if not is_changed and t_row != row:
                    is_changed = True
            
            final_max = max(max_in_move, curr_max)
            if final_max > ans[0]:
                ans[0] = final_max

            if is_changed:
                dfs(count + 1, tuple(new_board), final_max)
            
            curr_board = tuple(zip(*curr_board[::-1]))

    dfs(0, initial_board, ans[0])
    print(ans[0])

solve()