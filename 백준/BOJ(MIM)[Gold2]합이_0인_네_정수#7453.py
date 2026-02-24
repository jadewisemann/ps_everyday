def solve():
    import sys

    raw_data = sys.stdin.read().split()
    n = int(raw_data[0])
    nums = list(map(int, raw_data[1:]))
    nums_a, nums_b, nums_c, nums_d = [nums[i::4] for i in range(4)]

    sums_ab = sorted([
        a + b
        for a in nums_a
        for b in nums_b
    ])

    sums_cd = sorted([
        c + d
        for c in nums_c
        for d in nums_d
    ], reverse= True)

    l, r = 0, 0
    ans = 0

    while l < n * n and r < n * n:
        curr_sum = sums_ab[l] + sums_cd[r]

        if curr_sum < 0:
            l += 1
        elif curr_sum > 0:
            r += 1
        else:
            tmp = sums_ab[l]
            cnt_ab = 0
            while l < n * n and sums_ab[l] == tmp:
                l += 1
                cnt_ab += 1
            
            tmp = sums_cd[r]
            cnt_cd = 0
            while r < n * n and sums_cd[r] == tmp:
                r += 1
                cnt_cd += 1
            
            ans += cnt_ab * cnt_cd

    print(ans)


def solve__dict():
    import sys

    raw_data = sys.stdin.read().split()
    n = int(raw_data[0])
    nums = list(map(int, raw_data[1:]))
    nums_a, nums_b, nums_c, nums_d = [nums[i::4] for i in range(4)]

    ab_dict = {}
    for a in nums_a:
        for b in nums_b:
            s = a + b
            if s in ab_dict:
                ab_dict[s] += 1
            else:
                ab_dict[s] = 1

    ans = 0
    for c in nums_c:
        for d in nums_d:
            target = -(c + d)
            if target in ab_dict:
                ans += ab_dict[target]

    print(ans)
