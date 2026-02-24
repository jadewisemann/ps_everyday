n = int(input())
arr = list(map(int, input().split()))

stk = []
rst = []

for _ in range(n):
    curr = arr.pop()
    
    while stk and stk[-1] <= curr:
        stk.pop()
    else:
        rst.append(stk[-1] if stk else "-1")
    
    stk.append(curr)

print(*(reversed(rst)))