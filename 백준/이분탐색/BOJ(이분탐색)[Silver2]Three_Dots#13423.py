import sys
input = sys.stdin.readline

def main():
    get_input = lambda: (int(input()), list(map(int, input().split())))

    def solve_bisect(n, arr):
        arr = sorted(arr)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                target = 2 * arr[j] - arr[i]

                low  = j + 1
                high = n - 1 
                is_found = False

                while low <= high:
                    mid = (low + high) // 2
                    
                    if arr[mid] == target:
                        is_found = True
                        break

                    elif arr[mid] < target: low  = mid + 1
                    elif arr[mid] > target: high = mid - 1

                if is_found: count += 1    

        return count

    def solve_bisect_lib(n, arr):
        from bisect import bisect_left

        arr = sorted(arr)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                target = 2 * arr[j] - arr[i]

                pos = bisect_left(arr, target, lo = j + 1)

                if pos < n and arr[pos] == target: count += 1

        return count

    def solve_hashset(n ,arr):
        arr = sorted(arr)
        set_arr = set(arr)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (2 * arr[j] - arr[i]) in set_arr:
                    count += 1
        
        return count

    for _ in range(int(input())):
        n, arr = get_input()
        # ans = solve_bisect(n, arr)
        # ans = solve_bisect_lib(n, arr)
        ans = solve_hashset(n, arr)
        print(ans)
        
if __name__ == "__main__":
    main()