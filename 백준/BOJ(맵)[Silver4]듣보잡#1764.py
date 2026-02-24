n, m = map(int, input().split())

aset = {input() for _ in range(n)}
bset = {input() for _ in range(m)}

aset &= bset

print(len(aset))
print('\n'.join(sorted(list(aset))))