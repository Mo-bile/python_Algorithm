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
    # return len(st) == 0 도 동일하게 가능
           
    return answer
