def solution(s):
    answer = True
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append("(")
        else:
            if stack :
                stack.pop()
            else :
                answer = False
                
    if stack :
        answer = False
                
    return answer
            
            