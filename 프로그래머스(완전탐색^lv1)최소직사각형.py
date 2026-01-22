def solution(sizes):
    mx, mn = 0, 0
    for  (x,y) in sizes:   
        tmx, tmn = (x, y) if x > y else (y, x)
        mx = tmx if tmx > mx else mx
        mn = tmn if tmn > mn else mn

    return(mx*mn)

def solution_2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)