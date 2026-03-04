def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    plus_lmt, minus_lmt, multi_lmt, divid_lmt = map(int, input().split())

    global_max = - 1_000_000_001
    global_min = 1_000_000_001

    def operate(curr_val, curr_idx, plus, minus, multi, divid):
        nonlocal global_max, global_min
        
        if curr_idx == n:
            if curr_val > global_max:
                global_max = curr_val
            
            if curr_val < global_min:
                global_min = curr_val
            return 
        
        if plus < plus_lmt:
            new_val = curr_val + nums[curr_idx]
            operate(new_val, curr_idx + 1, plus + 1, minus, multi, divid)

        if minus < minus_lmt:
            new_val = curr_val - nums[curr_idx]
            operate(new_val, curr_idx + 1, plus, minus + 1, multi, divid)

        if multi < multi_lmt:
            new_val = curr_val * nums[curr_idx]
            operate(new_val, curr_idx + 1, plus, minus, multi + 1, divid)

        if divid <  divid_lmt:
            new_val = int(curr_val / nums[curr_idx])
            operate(new_val, curr_idx + 1, plus, minus, multi, divid + 1)

    operate(nums[0], 1, 0, 0, 0, 0)

    print(global_max)
    print(global_min)

solve()
