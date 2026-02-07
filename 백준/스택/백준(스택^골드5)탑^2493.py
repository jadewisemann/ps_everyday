t = int(input())
arr = list(map(int, input().split()))
stk = []
rst = []

for idx in range(t):
    curr = arr[idx]

    while stk and stk[-1][1] < curr:
        stk.pop()
    
    if not stk:
        rst.append(0)
    else:
        rst.append(stk[-1][0])
        
    stk.append((idx+1, curr))

print(" ".join(map(str, rst)))