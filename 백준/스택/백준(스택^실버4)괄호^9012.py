for _ in range(int(input())):
    stk = []
    ans = None
    for char in list(input()):
        if char == '(':
            stk.append(char)
        else:
            if not stk:
                ans = 'NO'
                break
            stk.pop() 

    print('NO' if stk else 'YES' if ans is None else ans)