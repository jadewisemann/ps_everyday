def solve():
    n = int(input())

    probs = [
        [int(x) / 100 for x in input().split()]
        for _ in range(n)
    ]

    max_val_per_row = [max(row) for row in probs]   
        
    suffix_max = [1.0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_max[i] = suffix_max[i + 1] * max_val_per_row[i]

    max_prob = 0.0
    used_job = [False] * n


    def choose(curr_idx, curr_prob):
        nonlocal max_prob
        
        # pruning
        if curr_prob * suffix_max[curr_idx] <= max_prob: return
        
        # base condition
        if curr_idx == n:
            max_prob = max(max_prob, curr_prob)
            return

        for job_idx in range(n):
            if used_job[job_idx]: continue
            if probs[curr_idx][job_idx] <= 0: continue
            used_job[job_idx] = True
            choose(curr_idx + 1, curr_prob * probs[curr_idx][job_idx])
            used_job[job_idx] = False

    choose(0, 1.0)

    return max_prob


def main():
    for tc in range(int(input())):
        ans = solve()
        print(f'#{tc+1} {ans*100:.6f}')

if __name__ == "__main__":
    main()