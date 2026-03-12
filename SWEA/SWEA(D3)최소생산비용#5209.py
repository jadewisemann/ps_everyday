def solve():
    n = int(input())
    merchs = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    min_sum = 1486 #99 * 15 + 1

    produced = [False] * n

    def choose(curr_idx, curr_sum):
        nonlocal min_sum
        
        # base condition
        if curr_idx >= n: 
            if curr_sum < min_sum:
                min_sum = curr_sum
            return

        # pruning
        if curr_sum >= min_sum: return

        # send to next state
        for i in range(n):
            if produced[i]: continue
            
            produced[i] = True
            choose(curr_idx + 1, curr_sum + merchs[curr_idx][i])
            produced[i] = False

    choose(0, 0)
    return min_sum
    
def main():
    for tc in range(int(input())):
        ans = solve()
        print(f'#{tc + 1} {ans}')

if __name__ == "__main__":
    main()

