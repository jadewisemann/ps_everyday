n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = set()

def a(nums, idxs):
    if len(nums) == m:
        result.add(nums)
        return

    for i in range(n):
        if i not in idxs:
            a(nums + (arr[i],), idxs + (i,))

a((), ())
for el in sorted(result):
    print(*el)