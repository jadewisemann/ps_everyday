w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
    
x = w - abs(w - (p + t) % (2 * w))
y = h - abs(h - (q + t) % (2 * h))

print(x, y)