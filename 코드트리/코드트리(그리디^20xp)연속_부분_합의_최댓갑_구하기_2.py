n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
curr = 0
sums = a[0]

for el in a:
    curr += el

    if curr > sums:
        sums = curr
    
    if curr < 0:
        curr = 0

print(sums)