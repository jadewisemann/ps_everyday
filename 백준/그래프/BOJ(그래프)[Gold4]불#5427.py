def main():
    tokens = iter(open(0).read().split())
    
    out = []
    out_append = out.append
    
    for _ in range(int(next(tokens))):
        w = int(next(tokens))
        h = int(next(tokens))
        
        grid = []
        grid_append = grid.append
        q = []
        q_append = q.append
        
        for _ in range(h):
            for char in next(tokens):
                if char == '.':
                    grid_append(-1)
                elif char == '#':
                    grid_append(1)
                elif char == '*':
                    q_append((len(grid), 1))
                    grid_append(1)
                else: 
                    start_pos = (len(grid), 0)
                    grid_append(0)
            grid_append(2) 
            
        w += 1 
        grid += [2] * w 
        
        q_append(start_pos) 
        
        t = 0
        ans = "IMPOSSIBLE"
        
        w_neg = -w
        w_pos = w
        
        while q and q[-1][1] == 0:
            current_q = q
            q = []
            q_append = q.append
            t += 1
            
            escaped = False
            for ci, state in current_q:
                
                ni = ci - 1
                if grid[ni] < state: 
                    grid[ni] = state
                    q_append((ni, state))
                elif state | grid[ni] == 2: 
                    ans = str(t)
                    escaped = True
                    break
                    
                ni = ci + 1
                if grid[ni] < state: 
                    grid[ni] = state
                    q_append((ni, state))
                elif state | grid[ni] == 2: 
                    ans = str(t)
                    escaped = True
                    break
                    
                ni = ci + w_neg
                if grid[ni] < state: 
                    grid[ni] = state
                    q_append((ni, state))
                elif state | grid[ni] == 2: 
                    ans = str(t)
                    escaped = True
                    break
                    
                ni = ci + w_pos
                if grid[ni] < state: 
                    grid[ni] = state
                    q_append((ni, state))
                elif state | grid[ni] == 2: 
                    ans = str(t)
                    escaped = True
                    break
                
            if escaped:break
                
        out_append(ans)
            
    print('\n'.join(out))

if __name__ == '__main__':
    main()