def solution(s):
    answer = True
    
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                
    if stack :
        answer = False;
        
           
    return answer