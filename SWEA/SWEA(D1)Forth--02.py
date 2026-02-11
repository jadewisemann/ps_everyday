for tc in range(int(input())):
    stck, res = [], 'error'

    for elem in input().split():
        if elem.isdigit():
            stck.append(elem)

        elif elem in "+-*/":
            if len(stck) < 2:
                break
            
            b, a = stck.pop(), stck.pop()
            stck.append(str(eval(f"{a}{elem if elem != '/' else '/'}{b}")))

        elif elem == "." and len(stck) == 1:
            res = stck.pop()

    print(f'#{tc + 1} {res}')
        