def get_data():
    n, m = map(int, input().split())
    ww = list(map(int, input().split()))
    tt = list(map(int, input().split()))
    return n, m, ww, tt

def solve():
    n, m, ww, tt = get_data()
    
    ww.sort(reverse=True)
    tt.sort(reverse= True)
    ti = 0
    cnt = 0
    for w in ww:
        if ti <m and w <= tt[ti]:
            cnt += w
            ti += 1

    return cnt
        

def main():
    for tc in range(int(input())):
        ans = solve()
        print(f'#{tc + 1} {ans}')


if __name__ == "__main__":
    main()