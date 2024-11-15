from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용


def find_max_queue_info():
    n = int(input().strip())
    queue = deque()
    max_count = 0
    min_last_student = None

    for _ in range(n):
        command = input().strip().split()
        if command[0] == '1':  # 학생이 줄을 섬
            student_num = int(command[1])
            queue.append(student_num)

            # 대기 학생 수와 마지막 학생 갱신 조건을 단순화
            if len(queue) > max_count:
                max_count = len(queue)
                min_last_student = student_num
            elif len(queue) == max_count and (min_last_student is None or student_num < min_last_student):
                min_last_student = student_num

        elif command[0] == '2':  # 식사가 준비되어 대기 중인 학생이 식사를 시작함
            queue.popleft()

    # 최종 결과 출력
    print(max_count, min_last_student)


# 함수 호출
find_max_queue_info()
