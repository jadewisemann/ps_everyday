from itertools import permutations

def solution(numbers):
    per  = permutations(numbers)
    # 수소 판볊
    def is_prime(nums):
        for i in range(2,nums):
            if nums % i == 0:
                return False
        return True

    # 세기
    print(nums)
    count = 0
    for num in nums:
        if is_prime:
            count += 1
    
    return count


a = solution('17')
print(a)




