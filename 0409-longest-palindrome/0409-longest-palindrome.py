# from collections import deque
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_hash = {}

        for c in s:
            if c not in s_hash:
                s_hash[c] = 1
            else :
                s_hash[c] += 1
        print(s_hash)
        odd_found = False

        count = 0
        odd_found = False

        for value in s_hash.values():
            if value % 2 == 0:
                count += value  # 짝수 개수는 그대로 추가
            else:
                count += value - 1  # 홀수 개수에서 1을 빼고 추가
                odd_found = True  # 홀수가 있음을 표시

        if odd_found:
            count += 1  # 홀수가 하나라도 있으면 중앙에 하나를 추가 가능
        return count

# 2번째 방식
        # s_hash = dict(sorted(s_hash.items(), key=lambda item: item[1]))

        # count = 0
        # for key, value in s_hash.items():
        #     # if len(s_hash) == 1:
        #     #     count += s_hash[key]
        #     #     return count

        #     if value == 1 and count == 0:
        #         count += 1
        #     elif value != 1:
        #         if value % 2 == 1 : #홀수이면
        #             value -= 1
        #             odd_found = True  # 홀수가 있음을 표시
        #         count += value
                

        # if odd_found:
        #         count += 1  # 홀수가 하나라도 있으면 중앙에 하나를 추가 가능
        # return count

# 직접 값을 입력하는 방식
        # string = deque()
        # sorted_hash = dict(sorted(s_hash.items(), key=lambda item: item[1]))
        # print(sorted_hash)

        # if len(s_hash) == 1:
        #     for _ in range(sorted_hash[s[0]]):
        #         string.append(s[0])
        #     return len(string)

        # for key, value in sorted_hash.items():
        #     if value == 1 and not string :
        #         string.append(key)
        #     elif value != 1:
        #         for i in range(0, value, 2):
        #             print(i)

        #             string.appendleft(key)
        #             string.append(key)
        # print(string)

        # return len(string)