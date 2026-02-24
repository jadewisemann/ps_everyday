def d(n):
    return n + sum(int(digit) for digit in str(n))

generated_numbers = set()
for i in range(1, 10001):
    generated_numbers.add(d(i))

self_numbers = [i for i in range(1, 10001) if i not in generated_numbers]
for num in self_numbers:
    print(num)