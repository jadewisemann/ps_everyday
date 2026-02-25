def ccw(p1, p2, p3):
    tmp = (
        (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1])
        - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])
    )

    return (
        1 if tmp > 0 else 
        -1 if tmp < 0 else
        0
    )


def is_intersect(a, b, c, d):
    abc, abd = ccw(a, b, c), ccw(a, b, d)
    cda, cdb = ccw(c, d, a), ccw(c, d, b)

    if not (abc * abd <= 0 and cda * cdb <= 0): return False
    if not (abc * abd == 0 and cda * cdb == 0): return True

    if a > b: a, b = b, a
    if c > d: c, d = d, c
    return b >= c and d >= a


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

print(int(is_intersect((x1, y1), (x2, y2), (x3, y3), (x4, y4))))