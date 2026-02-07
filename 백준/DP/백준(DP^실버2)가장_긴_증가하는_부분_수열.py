n = int(input())
arr = list(map(int, input().split()))


tmp = [arr[0]]

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    
    while l <= r:        
        mid = (l + r) // 2
        if  arr[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1

    return l

for i in range(1, n):
    if arr[i] > tmp[-1]:
        tmp.append(arr[i])
    elif arr[i] < tmp[-1]:
        tmp[binary_search(tmp, arr[i])] = arr[i]

print(len(tmp))