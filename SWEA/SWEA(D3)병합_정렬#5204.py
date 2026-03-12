def solve():
    n = int(input())
    org = list(map(int, input().split()))

    cnt = 0
        
    def merge_sort(lst):
        nonlocal cnt
        
        length = len(lst)

        if length <= 1:
            return lst

        mid = length // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])

        if left[-1] > right[-1]:
            cnt += 1

        merged = []
        l, r = 0, 0

        l_len, r_len = len(left), len(right)
        
        while l < l_len and r < r_len:
            if left[l] <= right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])   
                r += 1

        merged.extend(left[l:])
        merged.extend(right[r:])

        return merged
    

    return merge_sort(org)[n//2], cnt

def main():
    for tc in range(int(input())):
        ans = solve()
        print(f'#{tc + 1}', *ans)

if __name__ == "__main__":
    main()