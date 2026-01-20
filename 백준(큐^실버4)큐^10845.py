qu =  []
for el in [input() for _ in range(int(input()))]:
    op_arr = el.split()
    if len(op_arr) == 2:
        op, value = op_arr
        qu.append(value)
    else:
        op = op_arr[0]
        if op == 'pop':
            print(qu.pop(0) if qu else -1)
        elif op == 'size':
            print(len(qu))
        elif op == 'empty':
            print(0 if qu else 1)
            #? print(int(bool(stk)))
        elif op == 'front':
            print(qu[0] if qu else -1) 
        elif op == 'back':
            print(qu[-1] if qu else -1) 
