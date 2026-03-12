def solve():
    n, *stations = map(int, input().split())

    min_charge_cnt = 50 + 1
    def chose(curr_idx, charge_cnt, remain):
        nonlocal min_charge_cnt

        # base condition
        if curr_idx == n - 1:
            if charge_cnt < min_charge_cnt:
                min_charge_cnt = charge_cnt
            return
        
        # pruning
        if charge_cnt >= min_charge_cnt: return

        # charge
        chose(curr_idx + 1, charge_cnt + 1, stations[curr_idx] - 1)

        # check possible process
        if remain < 1:  return

        chose(curr_idx + 1, charge_cnt, remain - 1)

    chose(1, 0, stations[0] - 1)

    return min_charge_cnt   

def solve_optimized():
    n, *stations = map(int, input().split())

    min_charge_cnt = 50 + 1
    def chose(curr_idx, charge_cnt):
        nonlocal min_charge_cnt

        # base condition
        if curr_idx >= n - 1:
            if charge_cnt < min_charge_cnt:
                min_charge_cnt = charge_cnt
            return
        
        # pruning
        if charge_cnt >= min_charge_cnt: return

        for i in range(1, stations[curr_idx] + 1):
            chose(curr_idx + i, charge_cnt + 1)

    chose(0, 0)

    return min_charge_cnt  - 1

def solve_greedy():
    n, *stations  = map(int, input().split())

    charge_cnt = 0
    limit_dist = 1 + stations[0]
    max_reachable_dist = 0

    for curr in range(2, n):
        if limit_dist >= n: break

        if curr + stations[curr - 1] > max_reachable_dist:
            max_reachable_dist = curr + stations[curr - 1]
        
        if curr == limit_dist:
            charge_cnt += 1
            limit_dist = max_reachable_dist
    
    return charge_cnt

def main():
    for tc in range(int(input())):
        ans = solve_greedy()
        print(f'#{tc  + 1} {ans}')

if __name__ == "__main__":
    main()

