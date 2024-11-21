import sys
from heapq import heappush, heappop

# 1. N 후보 입력, N만큼 M 반복입력
N = int(sys.stdin.readline())
candidates = []

# 1-1. 다솜입력
dasom = int(sys.stdin.readline())

for _ in range(N - 1):
    # 최대힙으로 - 붙임
    M = (-int(sys.stdin.readline()))
    heappush(candidates, M)

answer = 0
while True:
    if len(candidates) == 0:
        break

    max_votes = (-heappop(candidates))
    if dasom <= max_votes:
        answer += 1
        dasom += 1
        max_votes -= 1
        heappush(candidates, -max_votes)
    else:
        break

sys.stdout.write(str(answer))

# # 튜플 방식으로 생각 했을 때
# # 2. maxheap 으로 tuple로 저장
# for _ in range(N):
#     M = int(sys.stdin.readline())
#     heappush(candidates, (_,M))
#
# print(candidates)
#
# # 3. 1순위 후보가 최대값 인지 검증 후 아니면 다른 1등 에서 1을 빼고, 1순위에 1추가
# for i in range(1, len(candidates)):
#     if candidates[0][1] < candidates[i][1]:
