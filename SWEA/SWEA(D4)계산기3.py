priority = {'*':2, '+':1, '(':0}

for t in range(1, 11):
    input()

    post, stck = [], [],

    for char in input():
        if char.isdigit(): 
            post += [char]
        elif char == '(':
            stck += [char]
        elif char == ')':
            while stck[-1] != '(':
                post += [stck.pop()]
            stck.pop()
        else:
            while stck and priority[stck[-1]] >= priority[char]:
                post += [stck.pop()]
            stck += [char]
    
    post += stck[::-1]

    res = []

    for char in post:
        if char.isdigit():
            res += [int(char)]
        else:
            v = res.pop()
            res[-1] = res[-1] * v if char == '*' else res[-1] + v
            
    print(f"#{t} {res[0]}")