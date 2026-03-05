get_input = lambda: (int(input()), list(map(int, input().split())))
calc_validity = lambda a, b, c, d: (a + b)**2 + (c + d)**2
mapper = lambda arr, *v: (arr[i] for i in v)

def solve(n, stations):
    return max(
        f(*mapper(stations, i, j, k, l))
        for i in range(n - 3)
        for j in range(i + 2, n - 2)
        for k in range(j + 2, n - 3)
        for l in range(k + 2, n)
        if not (i == 0 and l == n - 1)
        for f in (
            lambda a, b, c, d: calc_validity(a, b, c, d),
            lambda a, b, c, d: calc_validity(a, d, b, c)
        )
    )

def main():
    for tc in range(int(input())):
        print(f'#{tc + 1} {solve(*get_input())}')

if __name__ == "__main__":
    main()