n = int(input())
arr = list(map(int, input().split()))

idx_dict = {
    k: v for v, k in enumerate(sorted(set(arr)))
}

print(*(idx_dict[el] for el in arr))
