def solve(): 
    n = int(input())
    arr = list(map(int, input().split()))

    def quick_sort_iterative(arr, low, high):
        stack = [(low, high)]
        
        while stack:
            l, r = stack.pop()
            if l >= r: continue
            
            mid = (l + r) // 2
            
            if arr[l]   > arr[mid]: arr[l],   arr[mid] = arr[mid], arr[l]
            if arr[l]   > arr[r]:   arr[l],   arr[r]   = arr[r],   arr[l]
            if arr[mid] > arr[r]:   arr[mid], arr[r]   = arr[r],   arr[mid]
            
            arr[l], arr[mid] = arr[mid], arr[l]
            pivot = arr[l]
            
            i = l + 1
            j = r
            while i <= j:
                while i <= j and arr[i] <= pivot: i += 1
                while i <= j and arr[j] >= pivot: j -= 1
                
                if i < j: 
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            
            arr[l], arr[j] = arr[j], arr[l]
            p = j

            if p - l > r - p:
                stack.append((l, p - 1))
                stack.append((p + 1, r))
            else:
                stack.append((p + 1, r))
                stack.append((l, p - 1))

    quick_sort_iterative(arr, 0, n - 1)
    return n, arr

if __name__ == "__main__":
    for tc in range(int(input())):
        n, sorted_arr = solve()
        print(f"#{tc + 1} {sorted_arr[n // 2]}")