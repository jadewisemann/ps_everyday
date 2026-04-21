def solve():
    n, m = map(int, input().split())

    v_n, v_m = {n: 0}, {m: 0}
    q_n, q_m = {n}, {m}
    
    root_v = v_n

    while q_n and q_m:
        if len(q_n) > len(q_m):
            q_n, q_m, v_n, v_m = q_m, q_n, v_m, v_n

        next_level = set()
        is_forward = (v_n is root_v)

        for curr in q_n:
            if is_forward:
                ops = (curr + 1, curr - 1, curr * 2, curr - 10)
            else:
                ops = [curr - 1, curr + 1, curr + 10]
                if curr % 2 == 0: ops.append(curr // 2)

            for nxt in ops:
                if 0 <= nxt <= 1000000 and nxt not in v_n:
                    if nxt in v_m:
                        return v_n[curr] + 1 + v_m[nxt]
                    
                    v_n[nxt] = v_n[curr] + 1
                    next_level.add(nxt)
        q_n = next_level
    return -1

def main():
    for tc in range(1, int(input()) + 1):
        print(f'#{tc} {solve()}')

if __name__ == "__main__":
    main()