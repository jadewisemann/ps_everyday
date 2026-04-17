
def solve():
    d, w, k = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _ in range(d)
    ]
    
    def check():
        for j in range(w):
            passed = False
            cnt = 1

            if k == 1: passed = True

            for i in range(1, d):
                if grid[i][j] == grid[i - 1][j]:
                    cnt += 1
                else:
                    cnt = 1
                
                if cnt >= k:
                    passed = True
                    break
            
            if not passed: return False

        return True
    
    min_cnt = 14
    
    def recur(idx, curr_cnt):
        nonlocal min_cnt

        # pruning
        if curr_cnt >= min_cnt:
            return
        
        if idx == d:
            if check():
                if curr_cnt < min_cnt:
                    min_cnt = curr_cnt
            return
        
        recur(idx + 1, curr_cnt)

        org_raw = grid[idx][:]
        
        grid[idx] = [0] * w
        recur(idx + 1, curr_cnt + 1)

        grid[idx] = [1] * w
        recur(idx + 1, curr_cnt + 1)
        
        grid[idx] = org_raw

    if k == 1 or check():
        return 0
    
    recur(0, 0)
    
    return min_cnt



if __name__ == '__main__':
    for tc in range(int(input())):
        ans = solve()
        print(f'#{tc + 1} {ans}')
