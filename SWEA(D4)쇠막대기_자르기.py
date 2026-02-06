for tc in range(1, int(input())+ 1):
    stk, cnt, rst = [], 0, 0

    for chr in input():
        if not stk or chr != ")":
            cnt += 1
            stk.append(chr)
            is_close = False

        if stk and chr == ")":
            stk.pop()
            cnt -= 1
            rst += 1 if is_close else cnt
            is_close = True 

    print(f'#{tc} {rst}')