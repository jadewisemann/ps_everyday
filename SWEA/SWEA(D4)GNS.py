mapper = {
    "ZRO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3,
    "FOR" : 4,
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9
}

mapper_invert = {
    0: "ZRO",
    1: "ONE",
    2: "TWO",
    3: "THR",
    4: "FOR",
    5: "FIV",
    6: "SIX",
    7: "SVN",
    8: "EGT",
    9: "NIN"
}

for tc in range(1, int(input()) + 1):
    _ = input()
    arr = [mapper[el] for el in input().split()]
    arr.sort()
    print(f'#{tc}')
    print(*[mapper_invert[el] for el in arr])