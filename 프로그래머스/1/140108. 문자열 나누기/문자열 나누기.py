def solution(s):
    result = 0
    while s:
        count = 0
        move = 0
        for c in s :
            if c == s[0] :
                count += 1
            else : 
                count -= 1
            move += 1 
            if count == 0 :
                break
        result += 1
        s = s[move:]
    return result