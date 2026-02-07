str  = input()

stk = []
cnt = 0
rst = 0

for chr in str:
    if not stk or chr != ")":
        cnt += 1
        stk.append(chr)
        is_close = False

    if stk and chr == ")":
        stk.pop()
        cnt -= 1

        rst += 1 if is_close else cnt
        
        is_close = True 

print(rst)