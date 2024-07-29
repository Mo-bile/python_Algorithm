def solution(s):
    buffer = []
    
    for i in range(len(s)):
        if i == 0 and s[i] == ')':
            return False
        
        if s[i] == '(' :
            buffer.append('(')
        else :
            if len(buffer) == 0:
                return False
            else:
                buffer.pop()
            
    if len(buffer) == 0:
        return True
    else :
        return False

            
            