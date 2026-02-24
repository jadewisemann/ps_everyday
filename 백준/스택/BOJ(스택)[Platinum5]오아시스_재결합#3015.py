# I = lambda: int(input())
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
ans = 0
stk = []

for curr in arr:
    
    while stk and stk[-1][0] < curr:
        ans += stk.pop()[1]
    
    if stk and stk[-1][0] == curr:
        cnt = stk.pop()[1]
        ans += cnt

        if stk:
           ans += 1
         
        stk.append((curr, cnt + 1))
    
    else:
        if stk:
            ans += 1
        
        stk.append((curr, 1))

print(ans)

" ".join(etet)