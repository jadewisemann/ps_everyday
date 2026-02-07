n  = int(input())

for _ in range(n):
  _, *curr_a = list(map(int, input().split()))
  _, *curr_b = list(map(int, input().split()))
  
  for j in range(4, 0, -1):
    cnt_a = curr_a.count(j)
    cnt_b = curr_b.count(j)
    
    if cnt_a > cnt_b:
      print("A")
      break
    elif cnt_a < cnt_b:
      print("B")
      break
  else:
    print("D")
