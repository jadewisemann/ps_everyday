from collections import deque

def main():
    for tc in range(int(input())):
        n, e = map(int, input().split())
        it = iter(map(int, input().split()))

        grp = [[] for _ in range(n+1)]
        for _ in range(e):
            grp[next(it)].append(next(it))
        
        s, g = map(int, input().split())

        cnt = 0
        vis = {s}

        def dfs(curr):
            nonlocal cnt

            if curr == g:
                cnt += 1
                return
            
            for nxt in grp[curr]:
                if nxt in vis: continue
                vis.add(nxt)
                dfs(nxt)
                vis.remove(nxt)

        dfs(s)    
        print(f'#{tc + 1} {cnt}')

if __name__ == "__main__":
    main()