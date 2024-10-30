def solution(t, p):
    p_length = int(len(p)) # 3
    p_value = int(p) # 271
    result = 0
    
    for i in range(len(t)):
        if len(t) + 1 <= i + p_length :
            break
        else :
            sub = int(t[i : i + p_length])
            print(sub)
            if p_value >= sub :
                result += 1
            
    
    return result
                
        
        