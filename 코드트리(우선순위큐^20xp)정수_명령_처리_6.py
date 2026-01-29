import heapq

N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))


# Please write your code here.
hq  = []
for command in commands:
    if len(command) == 2:
        c, v  = command 
        heapq.heappush(hq, -v)
    if command[0] == "pop":
        pop = heapq.heappop(hq)
        print(-pop)
    elif command[0] == "size":
        print(len(hq))
    elif command[0] == "empty":
        print(0 if hq else 1)
    elif command[0] == "top":
        print(-hq[0])