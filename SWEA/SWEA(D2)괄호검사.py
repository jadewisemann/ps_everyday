for tc in range(int(input())):
    stc = []
    res = 1
    for char in input():
        if char not in '{()}':
            continue
        if char in '({':
            stc.append(char)
        elif char in ')}':
            if not stc:
                res = 0 
                break
                
            top = stc.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{'): 
                res = 0
                break
    if stc:
        res = 0

    print(f'#{tc + 1} {res }')