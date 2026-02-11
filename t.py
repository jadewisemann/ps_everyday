for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    x_cnt, y_cnt = 0, 0
    for x in range(x1, p1+1):
        if x2 <= x <= p2:
            x_cnt += 1
        if x_cnt > 1:
            break
    for y in range(y1, q1+1):
        if y2 <= y <= q2:
            y_cnt += 1
        if y_cnt > 1:
    if not x_cnt and not y_cnt:
        code = 'd'
    elif x_cnt == 1 and y_cnt == 1:
        code = 'c'
    elif x_cnt == 1 or y_cnt == 1:
        code = 'b'
    else:
        code = 'a'

    print(code)