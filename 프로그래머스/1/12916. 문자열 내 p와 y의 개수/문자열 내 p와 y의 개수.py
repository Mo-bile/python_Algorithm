def solution(s):
    
    s = s.lower()
    # if 'p' not in s and 'y' not in s :
    #     return False
    
    p_num = 0
    y_num = 0
    
    for char in s:
        if 'p' in char :
            p_num += 1
        elif 'y' is char :
            y_num += 1
    
    if p_num == y_num :
        return True
    else :
        return False