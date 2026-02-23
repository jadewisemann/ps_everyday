from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
nums = list(map(int, input().split()))

dq = deque([])
res = []

for i in range(n):
    if dq and dq[0] < i -  l + 1:
        dq.popleft()
    
    while dq and nums[dq[-1]] > nums[i]:
        dq.pop()
    
    dq.append(i)

    print(nums[dq[0]], end=' ')