k, n = map(int, input().split())
nums = [input() for _ in range(k)]
nums += [max(nums, key = int)] * (n - k)
nums.sort(key=lambda x : x * 10, reverse = True)

res = "".join(nums)
print(res if res[0] != 0 else '0')
