from itertools import accumulate as acc

for tc in range(int(input())):
    n = int(input())
    carot = list(map(int, input().split()))
    
    total = sum(carot)

    print(f'#{tc + 1}', *min(
        (
            (i + 1, abs(total - 2*s))
            for i, s in enumerate(acc(carot[:-1]))
        ), key=lambda x: x[1]
    ))