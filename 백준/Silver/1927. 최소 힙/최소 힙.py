import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    X = int(sys.stdin.readline())

    if X == 0 :
        if not heap:
            sys.stdout.write("0\n")
            continue
        sys.stdout.write(str(heapq.heappop(heap))+"\n")
        continue
    heapq.heappush(heap, X)
