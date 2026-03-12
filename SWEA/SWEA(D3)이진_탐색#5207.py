def solve():
    n, _ = map(int, input().split())
    nn = sorted(list(map(int, input().split())))
    mm = list(map(int, input().split()))

    cnt = 0
    for target in mm:
        l, r = 0, n - 1
        last_dir = 0
        is_possible = True

        while l <= r:
            mid = (l + r)// 2
            curr = nn[mid]
            if curr == target:
                cnt += 1
                break

            elif curr > target:
                if last_dir == 1: break
                r = mid - 1
                last_dir = 1

            elif curr < target:
                if last_dir == 2: break
                l = mid + 1
                last_dir = 2

    return cnt

def main():
    for tc in range(int(input())):

        ans = solve()
        print(f'#{tc + 1} {ans}')


if __name__ == "__main__":
    main()