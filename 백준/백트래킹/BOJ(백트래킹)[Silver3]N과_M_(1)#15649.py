

def solve(nums, used, m, curr_idx, his) -> None:
    
    # base conditino
    if m == curr_idx:
        print()

    solve()

    print()

def main():
    n, m = map(int, input().split())
    nums = [i + 1 for i in range(n)]
    used = [False for _ in range(n)]
    solve(nums, used, m, '')
if __name__ == '__main__':
    main()
