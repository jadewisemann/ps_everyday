from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for comb in combinations(arr, 3):
    s = sum(comb)
    if s <= m:
        ans = max(ans, s)
print(ans)