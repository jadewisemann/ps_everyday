stk =  []
for el in [input() for _ in range(int(input()))]:
    op_arr = el.split()
    if len(op_arr) == 2:
        op, value = op_arr
        stk.append(value)
    else:
        op = op_arr[0]
        if op == 'pop':
            print(stk.pop() if stk else -1)
        elif op == 'size':
            print(len(stk))
        elif op == 'empty':
            print(0 if stk else 1)
            #? print(int(bool(stk)))
        elif op == 'top':
            print(stk[-1] if stk else -1) 
