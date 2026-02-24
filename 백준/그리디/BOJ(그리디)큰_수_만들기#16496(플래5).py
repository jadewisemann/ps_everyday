_ = int(input())
print(int("".join(sorted(input().split(), key= lambda x: x * 10, reverse= True))))