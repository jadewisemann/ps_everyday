n = int(input())
arr = list(map(int, input().split()))

count = [0] * 10
max_lenght, l, kind = 0, 0, 0

for r in range(n):
    if count[arr[r]] == 0:
       kind += 1
    count[arr[r]] += 1

    while kind > 2:
        count[arr[l]] -= 1
        if count[arr[l]] == 0:
            kind -= 1
        l += 1
    
    if r - l + 1 > max_lenght:
        max_lenght = r - l + 1

print(max_lenght)