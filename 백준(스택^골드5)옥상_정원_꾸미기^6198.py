I = lambda: int(input())

arr = [[1, I()] for _ in range(I())]
counter = 0
stk = []

while arr:
    c, curr = arr.pop()
    
    while stk and curr > stk[-1][1]:
            a , _= stk.pop()
            c += a
            counter += a
    
    stk.append([c,curr])

print(counter)