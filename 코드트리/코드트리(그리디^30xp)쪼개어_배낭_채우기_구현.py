N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.

pwrs = [(av/aw, aw) for aw, av in  zip(w,v)]
pwrs.sort(key= lambda x: -x[0])

rst = 0
curr = M
for pwr, aw in pwrs:
    
    if curr > aw:
        rst += pwr * aw
        curr -= aw
    else:
        rst += pwr * curr
        break

print(f'{rst:.3f}')
