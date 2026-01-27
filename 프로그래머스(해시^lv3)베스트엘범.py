
def solution(genres, plays):
    n = len(genres)
    gen = {}
    total_count = {}
    rst = []

    for i in range(n):
        genre = genres[i]
        play = plays[i]
        
        gen.setdefault(genre, []).append([i, play])
        total_count[genre] = total_count.get(genre, 0) + play
        
    sorted_genres = sorted(total_count.items(), key=lambda x: x[1], reverse=True)
    total_keys = [k for k, p in sorted_genres]

    for key in total_keys:
        sorted_songs = sorted(gen[key], key=lambda x: (-x[1], x[0]))
        rst.extend([i for i, p in sorted_songs[:2]])

    return rst

    