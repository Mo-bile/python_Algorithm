import sys
from collections import deque

N = int(sys.stdin.readline().strip())

queue = deque(str(_) for _ in range(1, N + 1))

while queue:
    dump_card = queue.popleft()
    sys.stdout.write(f"{dump_card} ")
    # sys.stdout.write(dump_card)
    # sys.stdout.write(" ")

    if not queue:
        break
    store = queue.popleft()
    queue.append(store)