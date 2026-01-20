l = int(input())
input_str = str(input())

r = 31
m = 1234567891

sum = 0
for i in range(l):
    sum += (ord(input_str[i]) - 96) * (r ** i)

print(sum % m)
