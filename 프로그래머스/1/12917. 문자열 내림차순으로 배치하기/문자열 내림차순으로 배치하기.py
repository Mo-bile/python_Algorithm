def solution(s):
    result = sorted(s, reverse=True)
    answer = ''.join(result)
    return answer