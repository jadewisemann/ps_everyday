def solve():
    n = int(input())
    n_sq = n * n
    
    adj_list = []
    adj_empty = []
    for i in range(n):
        for j in range(n):
            idx = i * n + j
            neighbors = []
            if i > 0: neighbors.append(idx - n)
            if i < n - 1: neighbors.append(idx + n)
            if j > 0: neighbors.append(idx - 1)
            if j < n - 1: neighbors.append(idx + 1)
            adj_list.append(tuple(neighbors))
            adj_empty.append(len(neighbors))
    
    adj = tuple(adj_list)
    
    sit = [0] * n_sq
    student_sit = [-1] * (n_sq + 1)
    fav_map = [None] * (n_sq + 1)
    
    for _ in range(n_sq):
        row = input().split()
        student = int(row[0])
        favs = (int(row[1]), int(row[2]), int(row[3]), int(row[4]))
        fav_map[student] = favs
        
        favorites_adj = {}
        
        for favorite in favs:
            fsit = student_sit[favorite]
            if fsit >= 0:
                for adj_sit in adj[fsit]:
                    if not sit[adj_sit]:
                        if adj_sit in favorites_adj:
                            favorites_adj[adj_sit] += 1
                        else:
                            favorites_adj[adj_sit] = 1
                        
        if favorites_adj:
            best_sit = -1
            max_fa = 0
            max_em = -1
            
            for s, fa in favorites_adj.items():
                em = adj_empty[s]
                if fa > max_fa:
                    max_fa, max_em, best_sit = fa, em, s
                elif fa == max_fa:
                    if em > max_em:
                        max_em, best_sit = em, s
                    elif em == max_em:
                        if best_sit == -1 or s < best_sit:
                            best_sit = s
        else:
            best_sit = -1
            max_em = -1
            for s in range(n_sq):
                if not sit[s]:
                    em = adj_empty[s]
                    if em > max_em:
                        best_sit = s
                        max_em = em
                        if em == 4:
                            break
                            
        student_sit[student] = best_sit
        sit[best_sit] = student
        for adj_sit in adj[best_sit]:
            adj_empty[adj_sit] -= 1

    ans = 0
    score = (0, 1, 10, 100, 1000)
    
    for student in range(1, n_sq + 1):
        ss = student_sit[student]
        favs = fav_map[student]
        favorite_cnt = 0
        for sas in adj[ss]:
            if sit[sas] in favs:
                favorite_cnt += 1
        ans += score[favorite_cnt]

    print(ans)

if __name__ == '__main__':
    solve()