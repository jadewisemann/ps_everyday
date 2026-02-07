n = int(input())
t_shirts = list(map(int, input().split()))
t, p = map(int, input().split())

t_order =  0

for t_shirt in t_shirts:
    t_order += ((t_shirt - 1) // t) + 1

p_order_1 = n // p
p_order_2 = n % p

print(t_order)
print(p_order_1, p_order_2)