def get_input():
    n, m = input().split()
    lst = list(n)
    length = len(lst)
    return n, int(m), lst, length

def solve():
    n, m, _, length = get_input()
    
    max_num =  -1
    visited = set()

    def dfs(cnt, curr):
        nonlocal max_num    
        
        if (curr, cnt) in visited: return
        visited.add((curr, cnt))
         
        if cnt == m:
            max_num = max(max_num, int(curr))
            return

        curr_lst = list(curr)
        for i in range(length):
            for j in range(i + 1, length):
                curr_lst[i], curr_lst[j] = curr_lst[j], curr_lst[i]
                dfs(cnt + 1, "".join(curr_lst))
                curr_lst[i], curr_lst[j] = curr_lst[j], curr_lst[i]

    dfs(0, n)

    return max_num 

def solve_optimize():
    _, m, lst, length = get_input()

    max_val = 0
    visitied = set()

    best_str = "".join(sorted(lst, reverse=True))
    best_val = int(best_str)

    has_dup = len(set(lst)) < length
    
    def dfs(count):
        nonlocal max_val
        
        if max_val == best_val: return

        curr_str = "".join(lst) 

        if curr_str == best_str:
            if count % 2 == 0 or has_dup:
                max_val = max(max_val, best_val)
            else:
                if length >= 2:
                    lst[-1],lst[-2] = lst[-2], lst[-1]
                    max_val = max(max_val, int(''.join(lst)))
                    lst[-1],lst[-2] = lst[-2], lst[-1]
                else:
                    max_val = max(max_val, int(curr_str))
            return
        
        if count == 0:
            max_val = max(max_val, int(curr_str))
            return
        
        if (curr_str, count) in visitied: return

        visitied.add((curr_str, count))

        for i in range(length):
            for j in range(i + 1, length):
                lst[i], lst[j] = lst[j], lst[i]
                dfs(count -1)
                lst[i], lst[j] = lst[j], lst[i]

    dfs(m)
    return max_val


def main():
    for tc in range(int(input())):
        ans = solve_optimize()
        print(f'#{tc + 1} {ans}')

if __name__ == "__main__":
    main()