n = int(input())

# Please write your code here.

def a(n, curr):
    len_curr = len(curr)
    
    if len_curr > n:
        return 0
    elif len_curr == n:
        return 1
    
    return (
        a(n, curr + "1")
        + a(n, curr + "2" * 2)
        + a(n, curr + "3" * 3)
        + a(n, curr + "4" * 4)
    )



print(a(n, ""))