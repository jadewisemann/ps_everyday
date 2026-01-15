SIZE = 5

grp = [ n for _ in range(SIZE) for n in map(int, input().split())]
nums = [ n for _ in range(SIZE) for n in map(int, input().split())]

row_count = [0] * SIZE
col_count = [0] * SIZE
diag1, diag2 = 0, 0
bingo_total = 0


for i in range(SIZE*SIZE):
  num = nums[i]
  idx = grp.index(num)

  row, col  = idx // SIZE, idx % SIZE
  
  row_count[row] += 1
  if row_count[row] == SIZE:
    bingo_total += 1

  col_count[col] += 1
  if col_count[col] == SIZE:
    bingo_total += 1
  
  if row == col:
    diag1 += 1
    if diag1 == SIZE:
      bingo_total += 1
  if row + col == SIZE - 1:
    diag2 += 1
    if diag2 == SIZE:
      bingo_total += 1
    
  if bingo_total >= 3:
    print(i + 1)
    break