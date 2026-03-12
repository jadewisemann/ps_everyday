def solve_counting():
    data = map(int, input().split())

    max_val = 1000000
    counts = [0] * (max_val + 1)

    for num in data:
        counts[num] += 1

    target_index = 500000
    current_count = 0
    
    for i in range(1, max_val + 1):
        if counts[i] > 0:
            if current_count + counts[i] > target_index:
                print(i)
                return
            current_count += counts[i]

def solve_radix():
    data = list(map(int, input().split()))

    def radix_sort(arr):
        for i in range(3):
            buckets = [[] for _ in range(256)]
            shift = i * 8
            for num in arr:
                digit = (num >> shift) & 0xFF
                buckets[digit].append(num)
            
            arr = []
            for bucket in buckets:
                arr.extend(bucket)
        return arr

    sorted_A = radix_sort(data)
    print(sorted_A[500000])

if __name__ == "__main__":
    solve_radix()