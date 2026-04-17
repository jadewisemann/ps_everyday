from itertools import combinations

def solve():
    n = int(input())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    people, stairs = [], []
    
    for i in range(n):
        for j in range(n):
            if   grid[i][j] == 1: people.append((i, j))
            elif grid[i][j] >= 2: stairs.append((i, j, grid[i][j]))

    m = len(people)
    dists = [
        [
            abs(pr - sr) + abs(pc - sc)
            for sr, sc, _ in stairs
        ] 
        for pr, pc in people
    ]

    def get_time(arr, k):
        if not arr: return 0

        cq = [0, 0, 0] 
        
        for i, t in enumerate(sorted(arr)):
            idx = i % 3
            cq[idx] = max(t + 1, cq[idx]) + k
            
        return max(cq)

    ans = float('inf')
    
    all_people = set(range(m))

    for k in range(m + 1):
        for comb in combinations(range(m), k):
            time = get_time([dists[i][0] for i in comb], stairs[0][2])
            if time >= ans: continue

            ans = min(ans, max(time, get_time([dists[i][1] for i in all_people.difference(comb)], stairs[1][2])))

    return ans


if __name__ == '__main__':
    for tc in range(int(input())):
        print(f'#{tc+1} {solve()}')