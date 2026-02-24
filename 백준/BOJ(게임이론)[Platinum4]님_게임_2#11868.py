n = int(input())
arr = list(map(int, input().split()))

ans = 0
for k in arr:
    ans ^= k

print("koosaga" if ans else "cubelover")