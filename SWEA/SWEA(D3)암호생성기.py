for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))

    min_cycle = max(0, (min(nums) - 1) // 15)
    nums = [
        n - min_cycle * 15
        for n in nums
    ]
    
    cnt = 0
    while True:
        val = nums.pop(0) - (cnt % 5 + 1)
        
        if val <= 0:
            nums.append(0)
            break

        nums.append(val)
        cnt += 1


    print(f'#{tc}', *nums)