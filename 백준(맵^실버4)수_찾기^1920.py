n = int(input())
nums = {
    num: 1 for num in map(int, input().split())
}

m = int(input())
ans = list(map(int, input().split()))

for el in ans:
    print(nums.get(el, 0))