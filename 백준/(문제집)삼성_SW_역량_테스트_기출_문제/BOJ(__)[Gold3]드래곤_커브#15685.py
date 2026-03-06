n = int(input())
for _ in range(n):
    # x y d g
    # 시작점, 방향, 세대
    # 
    pass

rotate = lambda ri, rj, points: [(ri + (y - rj), rj - (x - ri)) for x, y in points]

memo = [[[] for _ in range(3)] for _ in range(10 + 1)]
def get_dragon_curv(dir, g):
    if memo[g][dir]:
        return memo[g][dir]
    
    *org, end = get_dragon_curv(dir, g - 1)
    rot = rotate(*end, org)
    memo[g][dir] = org + rot
    return memo[g][dir]



    

                  

