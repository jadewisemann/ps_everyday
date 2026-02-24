n = int(input())
nums = set(map(int, input().split()))

m = int(input())
ans = list(map(int, input().split()))

for el in ans:
    print(1 if el in nums else 0)