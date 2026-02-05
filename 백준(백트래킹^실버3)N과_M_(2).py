n, m = map(int, input().split())
nums = [i + 1 for i in range(n)]

result = []

def a(num_length, start_number):
    if num_length == m:
        print(" ".join(map(str, result)))
        return 
    
    for idx in range(start_number, n + 1):
        result.append(idx)
        a(num_length + 1, idx + 1)
        result.pop()

a(0, 1) 