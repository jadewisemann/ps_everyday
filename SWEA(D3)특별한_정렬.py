for tc in range(int(input())):
    n = int(input())
    arr = map(int, input().split())

    sorted_arr = sorted(arr)

    left_pointer, right_pointer = 0, n - 1
    rst = []
    
    while right_pointer >= left_pointer and len(rst) < 10:
        rst.append(sorted_arr[right_pointer])
        right_pointer -= 1.

        rst.append(sorted_arr[left_pointer])
        left_pointer += 1
    
    print(f"#{tc+1} {' '.join(map(str, rst))}")