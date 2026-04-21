def solve():
    for tc in range(int(input())):
        n = int(input())

        matrix = [
            list(map(int, input().split()))
            for _ in range(n)
        ]

        min_diff = float('inf')
        
        from itertools import combinations
        others = list(range(1, n))
        
        for combo in combinations(others, n // 2 - 1):
            a_group = [0] + list(combo)
            is_a = [False] * n
            for el in a_group:
                is_a[el] = True

            b_team = [
                el 
                for el in range(n) 
                if not is_a[el]
            ]
            
            a_sum = 0
            b_sum = 0
            
            half_n = n // 2
            for i in range(half_n):
                for j in range(i + 1, half_n):
                    u, v = a_group[i], a_group[j]
                    a_sum += matrix[u][v] + matrix[v][u]
                    
                    x, y = b_team[i], b_team[j]
                    b_sum += matrix[x][y] + matrix[y][x]
            
            diff = abs(a_sum - b_sum)

            if diff < min_diff: min_diff = diff
            if min_diff == 0: break
            
        print(f'#{tc + 1} {min_diff}')

solve()