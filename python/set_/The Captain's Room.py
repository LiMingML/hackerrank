# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


k = int(input())
rooms = list(map(int, input().split()))

room_counter = Counter(rooms)

for room, count in room_counter.items():
    if count == 1:
        print(room)
        break
