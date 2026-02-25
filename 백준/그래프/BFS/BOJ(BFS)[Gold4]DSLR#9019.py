import sys

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    
    lmt = 10_000
    for_table = [((2*i)%lmt, (i-1)%lmt, (i%1000)*10 + i//1000, (i%10)*1000 + i//10) for i in range(lmt)]
    
    rev_table = [[] for _ in range(lmt)]
    for i in range(lmt):
        d, s, l, r = for_table[i]
        rev_table[d].append((i, 'D'))
        rev_table[s].append((i, 'S'))
        rev_table[l].append((i, 'L'))
        rev_table[r].append((i, 'R'))

    results = []
    
    dist = [0] * lmt
    parent_for = [0] * lmt
    parent_rev = [0] * lmt

    for t in range(1, t + 1):
        A = int(input_data[2*t-1])
        B = int(input_data[2*t])
        
        if A == B:
            results.append("")
            continue

        dist[A] = t
        dist[B] = -t
        
        q_for = [A]
        q_rev = [B]
        
        meet_node = -1
        side = 0

        while q_for and q_rev:
            next_q = []
            for curr in q_for:
                for i, nxt in enumerate(for_table[curr]):
                    if dist[nxt] == t: continue
                    if dist[nxt] == -t:
                        meet_node = nxt
                        parent_for[nxt] = (curr << 8) | ord("DSLR"[i])
                        side = 1
                        break
                    dist[nxt] = t
                    parent_for[nxt] = (curr << 8) | ord("DSLR"[i])
                    next_q.append(nxt)
                if side: break
            if side: break
            q_for = next_q

            next_q = []
            for curr in q_rev:
                for nxt, op in rev_table[curr]:
                    if dist[nxt] == -t: continue
                    if dist[nxt] == t:
                        meet_node = nxt
                        parent_rev[nxt] = (curr << 8) | ord(op)
                        side = 2
                        break
                    dist[nxt] = -t
                    parent_rev[nxt] = (curr << 8) | ord(op)
                    next_q.append(nxt)
                if side: break
            if side: break
            q_rev = next_q

        path = []
        curr = meet_node
        while curr != A:
            val = parent_for[curr]
            path.append(chr(val & 0xFF))
            curr = val >> 8
        path.reverse()
        
        curr = meet_node
        while curr != B:
            val = parent_rev[curr]
            path.append(chr(val & 0xFF))
            curr = val >> 8
            
        results.append("".join(path))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()