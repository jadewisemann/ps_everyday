print("\n".join(
    [
        " ".join(x) for x in sorted(
            [input().split() for _ in range(int(input()))],
            key= lambda x: int(x[0])
        )
    ]
))