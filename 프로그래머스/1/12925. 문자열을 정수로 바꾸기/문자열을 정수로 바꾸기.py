def solution(s):
    # answer = 0
    # return answer
    if s.count('-') == 1:
        return -int(s[1:])
    else :
        return int(s)