from bisect import bisect_left

def get_lis_length(arr):
    lis = []
    positions = []

    for x in arr:
        idx = bisect_left(lis, x)
        if idx == len(lis):
            lis.append(x)
        else:
            lis[idx] = x
        positions.append(idx)

    return positions, len(lis)

def backtrack_lis(arr, positions, len_lis):
    result = []
    target_idx = len_lis - 1
    
    for i in range(len(arr) - 1, -1, -1):
        if positions[i] == target_idx:
            result.append(arr[i])
            target_idx -= 1
            
    return result[::-1]

def get_full_lis(arr):
    if not arr:
        return []

    positions, len_lis = get_lis_length(arr)

    return backtrack_lis(arr, positions, len_lis)
