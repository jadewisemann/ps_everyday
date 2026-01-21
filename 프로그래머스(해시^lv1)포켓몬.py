def solution(nums):
    n = len(nums)
    dict = {}
    for num in nums:
        dict[num] = dict.get(num, 0) + 1
    