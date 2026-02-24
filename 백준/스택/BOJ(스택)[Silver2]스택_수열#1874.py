n = int(input())

nums = [i + 1 for i in range(n)]

curr = 1
stk = []
rst = []
flag = True
for _ in range(n):
    target = int(input())

    while curr <= target:
        stk.append(curr)
        rst.append("+")
        curr += 1
    
    if stk[-1] == target:
        stk.pop()
        rst.append("-")
    
    else:
        flag = False
        break


print("\n".join(rst) if flag else "NO")