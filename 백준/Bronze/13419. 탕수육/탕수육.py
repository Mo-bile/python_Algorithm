import sys

def minimal_period(s):
    n = len(s)
    for p in range(1, n + 1):
        if n % p == 0 and s == s[:p] * (n // p):
            return s[:p]
    return s

def get_player_sequence(s, start):
    n = len(s)
    letters = []
    for i in range(n):
        index = (i * 2 + start) % n
        letters.append(s[index])
    sequence = ''.join(letters)
    return minimal_period(sequence)

T = int(sys.stdin.readline().strip())

for _ in range(T):
    s = sys.stdin.readline().strip()
    hwan = get_player_sequence(s, 0)  # 첫 번째 사람은 0부터 시작
    tae = get_player_sequence(s, 1)   # 두 번째 사람은 1부터 시작

    print(hwan)
    print(tae)


# import sys
#
# def find_min_rotation(s):
#     n = len(s)
#     double_s = s + s
#     return min(double_s[i : i + n] for i in range(n))
#
# # 무조건 이기기 위한 값?
# T = int(sys.stdin.readline().strip())
#
# # 어떻게 하면 기억해야할 문자열 중 가장 짧은 것을 출력할 수 있을까?
# for _ in range(T):
#     s = sys.stdin.readline().strip()
#     hwan = find_min_rotation(s) # 먼저
#     tae = find_min_rotation(s[::-1]) # 다음
#
#     print(hwan)
#     print(tae)
#
#
#
#     # # 우선 해당 문자열을 최대한 나열하고, 반복되는 지점을 찾는다.
#     # # 반복되는 직전까지를 가장 짧은 문자열로 뽑아낸다.
#     # i = 0
#     # while True :
#     #     turn_index = i % len(s)
#     #     if len(hwan) <= len(tae):
#     #         hwan.append(s[turn_index])
#     #     else :
#     #         tae.append(s[turn_index])
#     #
#     #     if i == 20:
#     #         break
#     #
#     #     i += 1