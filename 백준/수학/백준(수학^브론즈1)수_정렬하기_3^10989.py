import sys

ip = lambda: int(sys.stdin.readline())
nums = [0] * 10000

for _ in range(ip()):
    num = ip()
    nums[num-1] += 1

curr = 1
for el in nums:
    for _ in range(el):
        print(curr)
    curr += 1