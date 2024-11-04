import sys
from collections import defaultdict

# 1. 입력
N = int(sys.stdin.readline())

work_dict = defaultdict(int)
for i in range(4 * N):
    count = i % 4

    daily_workers = sys.stdin.readline().split()
    daily_workers_ = [worker for worker in daily_workers if worker != '-']
    # print(daily_workers_)

    if count == 0 or count == 2:
        for worker in daily_workers_:
            work_dict[worker] += 4
    elif count == 1 :
        for worker in daily_workers_:
            work_dict[worker] += 6
    elif count == 3:
        for worker in daily_workers_:
            work_dict[worker] += 10


# 2. dict 비교
# sorted_work_dict = sorted(work_dict.items(), key = lambda  item:item[1]) -> 필요없음
# print(sorted_work_dict)

# min = sorted_work_dict[0][1]
# max = sorted_work_dict[-1][1]

# min_hours = min(work_dict.values())
# max_hours = max(work_dict.values())

# differ = max_hours - min_hours
# print(differ)

if work_dict:
    min_hours = min(work_dict.values())
    max_hours = max(work_dict.values())
    differ = max_hours - min_hours
    if differ <= 12:
        sys.stdout.write("Yes")
        # print("Yes")
    else :
        sys.stdout.write("No")
        # print("No")
else :
    sys.stdout.write("Yes")
    # print("Yes")