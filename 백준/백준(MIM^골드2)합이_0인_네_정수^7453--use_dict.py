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
