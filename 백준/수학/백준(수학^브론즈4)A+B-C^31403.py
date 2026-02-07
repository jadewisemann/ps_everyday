ip = lambda: int(input())

a = ip()
b = ip()
c = ip()

print(a + b - c)
print(int(str(a) + str(b)) - c)