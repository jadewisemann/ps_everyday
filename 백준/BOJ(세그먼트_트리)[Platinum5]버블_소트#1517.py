n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))
rank_dict = {val: i + 1 for i, val in enumerate(sorted_arr)}
bit = [0] * (n + 1)

def update(i, delta):
    while i <= n:
        bit[i] += delta
        i += (i & -i)

def query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= (i & -i)
    return s

ans = 0
for i in range(n):
    rank = rank_dict[arr[i]]
    ans += i - query(rank)
    update(rank, 1)

print(ans)