def solve():    
    n = int(input())
    favs = [[] for _ in range(n * n + 1)]
    grid = [[[0] for _ in range(n)] for _ in range(n)]


    for _ in range(n * n):
        cc, *fav = map(int, input().split())
        favs[cc] = fav


        # 비어있는 칸찾기
        empty_cell = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    empty_cell.add((i, j))

        fav_cand = set()
        max_fav_cnt = 0
        # 1, 좋아하는 학생이 인접한 칸에 가장 많은 칸
        for i, j in empty_cell:
            fav_cnt = 0
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < n): continue
                if grid[ni][nj] in fav: fav_cnt += 1
            if fav_cnt > max_fav_cnt:
                fav_cand = set((i, j))
                max_fav_cnt = fav_cnt
            elif fav_cnt == max_fav_cnt:
                fav_cand.add((i, j))
        
        if len(fav_cand) == 1:
            i, j = fav_cand.pop()
            grid[i][j] = cc
            continue
    

        # 1이 여러개면
        empty_cand = set()
        max_empty_cnt = 0 
        for i, j in empty_cell:
            emtpy_cnt = 0
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < n): continue
                if grid[ni][nj] == 0: emtpy_cnt += 1
            if emtpy_cnt > max_empty_cnt:
                empty_cand = set((i, j))
                max_empty_cnt = emtpy_cnt
            elif emtpy_cnt == max_empty_cnt:
                empty_cand.add((i, j))
        
        if len(empty_cand) == 1:
            i, j = empty_cand.pop()
            grid[i][j] = cc
            continue

        # 여러개면
        i, j = sorted(list(empty_cand))[0]
        grid[i][j] = cc

    # 체점
    ans = 0
    for i in range(n):
        for j in range(n):
            curr = grid[i][j]
            sati_cnt = 0
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < n): continue
                if grid[ni][nj] in favs[curr]:
                    sati_cnt += 1
            
            ans += [0, 1, 10, 100, 1000][sati_cnt]

    print(ans)



if __name__ == '__main__':
    solve()