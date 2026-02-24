while True:
    ip = input()
    
    if ip == ".":
        break

    stk = []
    flag = "yes"

    for char in ip:        
        if char in "([":
            stk.append(char)

        elif char in ")":
            if not stk or stk.pop() != "(":
                flag = "no"
                break
        elif char == "]":
            if not stk or stk.pop() != "[":
                flag = "no"
                break
    
    if stk:
        flag = "no"
    
    print(flag)
