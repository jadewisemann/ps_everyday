import sys
input = sys.stdin.readline

all = [i + 1 for i in range(20)]
aset = set()
for _ in range(int(input())):
    tmp = input().split()
    command = tmp[0]
    value = int(tmp[1]) if len(tmp) > 1 else 0
    if command == 'add':
        aset.add(value)
    elif command == 'remove':
        if value in aset:
            aset.remove(value)
    elif command == 'check':
        print(int(value in aset))   
    elif command == 'toggle':
        if value not in aset:
            aset.add(value)
        else:
            aset.remove(value)
    elif command == 'all':
        aset = set(all)
    elif command == 'empty':
        aset = set()

    

