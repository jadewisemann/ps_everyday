def solve():
    n, m, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    max_kills = 0
    archers = []
    
    def backtrack(start_col):
        nonlocal max_kills
        
        if len(archers) == 3:
            current_kills = simulate(archers)
            if current_kills > max_kills:
                max_kills = current_kills
            return
            
        for col in range(start_col, m):
            archers.append(col)
            backtrack(col + 1)
            archers.pop()
            
    def simulate(archers):
        dead_enemies = set()
        total_kills = 0
        
        for turn in range(n):
            archer_row = n - turn 
            targets = set()
            
            for archer_col in archers:
                best_target = None
                min_dist = d + 1
                
                for i in range(archer_row - 1, -1, -1):
                    for j in range(m):
                        if board[i][j] == 0 or (i, j) in dead_enemies: continue
                            
                        dist = abs(archer_row - i) + abs(archer_col - j)
                        if dist > d: continue
                            
                        if dist < min_dist:
                            min_dist = dist
                            best_target = (i, j)
                        elif (
                            dist == min_dist and
                            best_target and 
                            j < best_target[1]
                        ):
                            best_target = (i, j)
                            
                if best_target:
                    targets.add(best_target)
                    
            for i, j in targets:
                if (i, j) not in dead_enemies:
                    dead_enemies.add((i, j))
                    total_kills += 1

        return total_kills

    backtrack(0)

    return max_kills

if __name__ == "__main__":
    ans = solve()
    print(ans)