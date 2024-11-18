import sys
import heapq

# 1. N, H, T 입력 /
N, H, T = map(int,sys.stdin.readline().split()) # map 으로 가능함
giants = []

# N. append
for _ in range(N):
    giants.append(int(sys.stdin.readline().strip()))

# 2. maxheap 정렬
max_heap = [-x for x in giants]
heapq.heapify(max_heap)

# 뿅망치 횟수
count = 0
for _ in range(T):
    # maxheap 의 1/2 로 줄이기
    max_value = - heapq.heappop(max_heap)
    if max_value < H:
        sys.stdout.write("YES\n"+str(count))
        sys.exit(0)
    if max_value == 1:
        heapq.heappush(max_heap, -max_value)
        break

    # heappush
    half_giant = max_value // 2
    heapq.heappush(max_heap, -half_giant)
    count += 1

# 판별

max_giant = -heapq.heappop(max_heap)
if H > max_giant:
    sys.stdout.write("YES\n"+str(count))
else:
    sys.stdout.write("NO\n" + str(max_giant))

