priority = {v: i for i, v in enumerate(["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"])}


for tc in range(1, int(input()) + 1):
    _ = input()
    print(f'#{tc}')
    print(*sorted(input().split(), key= lambda x: priority[x]))
