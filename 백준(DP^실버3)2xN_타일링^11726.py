SQ = [0, 1, 2]
n = int(input())
for idx in range(3, n+1):
    SQ.append((SQ[idx - 1] + SQ[idx - 2]) % 10007)
print(SQ[n])    