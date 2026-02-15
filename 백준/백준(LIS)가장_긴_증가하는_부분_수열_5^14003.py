import sys
input = sys.stdin.readline

from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

# get lis 
lis, position = [], []

for el in arr:
    idx = bisect_left(lis, el)

    if idx == len(lis):
        lis.append(el)
    else:
        lis[idx] = el

    position.append(idx)

res = []
curr_idx = len(lis) - 1

for i in range(n - 1, -1, -1):
    if position[i] == curr_idx:
        res.append(arr[i])
        curr_idx -= 1

print(len(lis))
print(*res[::-1])