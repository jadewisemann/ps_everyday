def solution(clothes):
    grp = {}

    for el in clothes:
        a, b = el
        grp.setdefault(b, []).append(a)

    rst = 1
    for k in grp.keys():
        rst *= (len(grp[k]) + 1)
    
    return rst -1


