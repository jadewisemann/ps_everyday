n = int(input())
arr = list(map(int, input().split()))

idx_dict = {
    k: v for v, k in enumerate(sorted(list(set(arr))))
}

for el in arr:
    print(idx_dict[el], end=" ")