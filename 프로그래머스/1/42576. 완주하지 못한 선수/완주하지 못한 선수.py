def solution(participant, completion):
    value = {}
    for p in participant:
        if value.get(p, 0) == 0:
            value[p] = 1
        else :
            value[p] += 1
    
    for c in completion:
        if value.get(c, 0) == 0:
            value[c] += 0
            
        else :
            value[c] -= 1
    
    
    for k, v in value.items():
        if v != 0 :
            return k
        
        