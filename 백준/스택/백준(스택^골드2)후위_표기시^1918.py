
stk = []
res = ""
prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

for char in input():
    if char.isalpha():
       res += char
    elif char == "(":
        stk.append(char)
    elif char == ")":
        while stk and stk[-1] != "(":
            res += stk.pop()
        stk.pop()
    else:
        while stk and prec[stk[-1]] >= prec[char]:
            res += stk.pop()
        stk.append(char)

while stk:
    res += stk.pop()

print(res)
        
