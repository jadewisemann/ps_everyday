l, c = map(int, input().split())
chars = sorted(input().split())

def dfs(curr_idx, path, vowel_cnt, consonant_cnt):
    if len(path) == l:
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print("".join(path))
        return
    
    for i in range(curr_idx, c):
        char = chars[i]
        is_vowel = char in "aeiou"
        dfs(i + 1, path + [char],vowel_cnt + is_vowel,  consonant_cnt + (not is_vowel))

dfs(0, [], 0, 0)