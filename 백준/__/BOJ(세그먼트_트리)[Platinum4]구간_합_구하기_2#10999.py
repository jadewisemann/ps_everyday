import sys

def solve():
    data = sys.stdin.read().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    prefix = [0] * (n + 1)
    cur_sum = 0
    for i in range(1, n + 1):
        cur_sum += int(data[i + 2])
        prefix[i] = cur_sum
        
    bit1 = [0] * (n + 1)
    bit2 = [0] * (n + 1)
    
    ptr = n + 3
    output = []
    
    _int = int
    _append = output.append
    
    for _ in range(m + k):
        q_type = data[ptr]
        if q_type == '1':
            l = _int(data[ptr+1])
            r = _int(data[ptr+2])
            diff = _int(data[ptr+3])
            ptr += 4
            
            i = l
            while i <= n:
                bit1[i] += diff
                i += i & -i
            i = r + 1
            while i <= n:
                bit1[i] -= diff
                i += i & -i
                
            v1 = diff * (l - 1)
            i = l
            while i <= n:
                bit2[i] += v1
                i += i & -i
            v2 = diff * r
            i = r + 1
            while i <= n:
                bit2[i] -= v2
                i += i & -i
        else:
            l = _int(data[ptr+1])
            r = _int(data[ptr+2])
            ptr += 3
            
            s1, s2, i = 0, 0, r
            while i > 0:
                s1 += bit1[i]
                s2 += bit2[i]
                i -= i & -i
            res_r = s1 * r - s2 + prefix[r]
            
            s1, s2, i = 0, 0, l - 1
            while i > 0:
                s1 += bit1[i]
                s2 += bit2[i]
                i -= i & -i
            res_l = s1 * (l - 1) - s2 + prefix[l - 1]
            
            _append(str(res_r - res_l))

    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    solve()