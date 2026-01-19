n = int(input())
bulbs = [*map(int, input().split())]

for _ in range(int(input())):
  sex, num = map(int, input().split())
  
  if sex == 1:
    for curr in range(num, n+1, num): 
      bulbs[curr-1] ^= 1 

  else:
    idx = num - 1
    bulbs[idx] ^= 1
    for i in range(1, n):
      if not (0 <= idx - i < n and 0 <= idx + i < n):
        continue  
      if bulbs[idx - i] == bulbs[idx + i]:
        bulbs[idx - i] ^= 1 
        bulbs[idx + i] ^= 1 
      
      else:
        break

for i in range(0, n , 20):
  print(*bulbs[i: i+20])