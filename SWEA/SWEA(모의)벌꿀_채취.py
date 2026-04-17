def solve():
    n, m, c = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    def calc_profit(honey, limit):
        num = len(honey)
        local_max_profit = 0

        def recur(idx, curr_sum, curr_profit):
            nonlocal local_max_profit

            # 가지 치기
            if curr_sum > limit:
                return

            # base
            if idx == num:
                if curr_profit > local_max_profit:
                    local_max_profit = curr_profit
                return
            
            curr_honey = honey[idx]
            recur(idx + 1, curr_sum + curr_honey, curr_profit + curr_honey **2)
            recur(idx + 1, curr_sum, curr_profit)
        
        recur(0, 0, 0)
        return local_max_profit            

    costs = [[0] * (n - m + 1) for _ in range(n)]
    for r in range(n):
        for col in range(n - m + 1):
            costs[r][col] = calc_profit(grid[r][col:col + m], c)   

    max_profit = 0
    for r1 in range(n):
        for c1 in range(n - m + 1):
            for r2 in range(r1, n):
                start_c2 = c1 + m if r1 == r2 else 0
                for c2 in range(start_c2, n - m + 1):
                    curr_profit = calc_profit(grid[r1][c1:c1 + m], c) + calc_profit(grid[r2][c2: c2 +m], c)
                    if curr_profit > max_profit:
                        max_profit = curr_profit

    return max_profit

if __name__ == '__main__':
    for tc in range(int(input())):
        ans = solve()
        print(f'#{tc + 1} {ans}')
    

    