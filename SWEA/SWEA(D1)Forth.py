for tc in range(int(input())):
    res = 'error'
    stck = []
    for elem in input().split():
        if elem.isdigit():
            stck.append(elem)

        elif elem in "+-*/":
            if len(stck) < 2:
                break
            nb, na = int(stck.pop()), int(stck.pop())
            stck.append(
                na * nb if elem == "*" else
                na + nb if elem == "+" else 
                na - nb if elem == "-" else
                na // nb
            )

        else:
            if stck and len(stck) == 1:
                res = stck.pop()
                
    print(f'#{tc + 1} {res}')
        