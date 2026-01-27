def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    a = []
    for i in range(r1):
        b = []
        for j in range(c2):
            tmp = 0
            for k in  range(c1):
                tmp += arr2[k][j] * arr1[i][k]
            b.append(tmp)
        a.append(b)
    
    return a