def solve():
    works = [
        tuple(map(int, input().split()))
        for _ in range(int(input()))
    ]
    
    works.sort(key = lambda x: x[1])
    
    cnt = 0
    end_pointer = 0

    for s, e in works:
        if s >= end_pointer:
            cnt += 1
            end_pointer = e

    return cnt

def main():
    for tc in range(int(input())):
        ans = solve()
        print(f'#{tc + 1} {ans}')

if __name__ == "__main__":
    main()