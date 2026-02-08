
stk = []
res = ""
for char in input():
    if char.isalpha():
       res += char
    elif char == "(":
        stk.append(char)
    elif char == ")":
        while stk[-1] == "(":
            res += stk.pop()
    else:
        while stk[-1] >= 
        # ? 
        
