n = int(input())
a, b, c, d, e, f = map(int, input().split())

if n == 1:
    print(sum([a, b, c, d, e, f]) - max(a, b, c, d, e, f))
else:
    ms = sorted([min(a, f), min(b, e), min(c, d)])
    m, mm, mmm = ms[0], ms[0] + ms[1], sum(ms)
    print(
        mmm * 4
        + mm * (8 * n - 12)
        + m * (5 * n**2 - 16 * n + 12)
    )
