count = 0
for _ in range(int(input())):
    stk = []

    for chr in input():
        if stk and stk[-1] == chr:
            stk.pop()
        else:
            stk.append(chr)
    
    count += 0 if stk else 1

print(count)