n = int(input())
plays = [
    list(map(int, input().split())) 
    for _ in range(n)
]

curr = 0
inning = 0
out_count = 0
score = 0
base = [False] * 5

while True:
    if inning >= n:
        break

    now = plays[inning][curr]

    if out_count >= 3:
        inning += 1
        base = [False] * 5
        continue

    if now == 0:
        out_count += 1
        continue
    
    for i in range(now, 0, - 1):
        if base[i] == True:
            base[i] = False
            if i + now >= 4:
                score += 1
            else:
                base[i + now] = True
            
    curr = (curr + 1) % 9            
print(score)