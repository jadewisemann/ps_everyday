for tc in range(int(input())):
    stk = []
    for char in input():
        if stk and stk[-1] == char:
            stk.pop()
        else:
            stk.append(char)
     
    print(f'#{tc + 1} {len(stk)}')