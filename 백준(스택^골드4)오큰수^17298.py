n = int(input())
arr = list(map(int, input().split()))

stk = []
rst = []

for i in range(n-1, -1, -1):
    curr = arr[i]
    
    while stk and stk[-1] <= curr:
        stk.pop()
    
    else:
        rst.append(stk[-1] if stk else "-1")
    
    stk.append(curr)

print(*(reversed(rst)))