n = int(input())
arr = list(map(int, input().split()))
rst = []
for idx in range(n):
  curr = idx + 1
  move = arr[idx]
  rst.insert(idx-move, curr)

print(*rst)