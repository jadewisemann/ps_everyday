ip = list(input().split('*'))

for i in range(10):
    if sum(w * int(d) for w, d in zip([1, 3] * 7, ip[0] + str(i) + ip[1])) % 10 == 0:
        print(i)
        break 