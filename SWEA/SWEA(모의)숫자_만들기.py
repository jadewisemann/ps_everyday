def main():
    n = int(input())
    p, m, mu, d = map(int, input().split())
    nums = list(map(int, input().split()))
    
    max_val = -100000001
    min_val = 100000001
    
    def dfs(idx, current_val, plus, minus, multi, div):            
        nonlocal max_val, min_val
        if idx == n:
            max_val = max(max_val, current_val)
            min_val = min(min_val, current_val)
            return

        if plus > 0:  dfs(idx + 1, current_val + nums[idx], plus - 1, minus, multi, div)
        if minus > 0: dfs(idx + 1, current_val - nums[idx], plus, minus - 1, multi, div)
        if multi > 0: dfs(idx + 1, current_val * nums[idx], plus, minus, multi - 1, div)
        if div > 0:   dfs(idx + 1, int(current_val / nums[idx]), plus, minus, multi, div - 1)

    dfs(1, nums[0], p, m, mu, d)

    return max_val - min_val

if __name__ == "__main__":
    for tc in range(int(input())):
        print(f"#{tc + 1} {main()}")
a