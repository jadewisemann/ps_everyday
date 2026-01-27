def solution(nums):
    lsn = len(set(nums))
    return min(len(nums)//2, lsn)