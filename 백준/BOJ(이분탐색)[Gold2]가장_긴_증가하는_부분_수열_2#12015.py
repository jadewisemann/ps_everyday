import bisect

n = int(input())
arr = list(map(int, input().split()))

l = [arr[0]]

for i in range(1, n):
    curr = arr[i]

    if curr > l[-1]:
        l.append(curr)
    
    else:
        idx = bisect.bisect_left(l, curr)
        l[idx] = curr

print(len(l))
