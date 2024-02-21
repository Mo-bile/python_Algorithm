"""" 문제 : 괄호 짝 확인하기"""

from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = deque() # 사용할 스택 정의
    # index = []
    for i in range(len(string)):
        char = string[i]
        if char == "(":
            stack.append(i)
            # index.append(i)
        elif char == ")":
            if stack :
                stack.pop()
                # index.pop()
            else :
                print(f"문자열 {i} 번째 위치에 있는 괄호에 맞는 열리는 괄호가 없습니다")

    while stack:
        print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다")

    # 잘못생각함
        # for char in string:
        #     stack.append(char)
        #
        # parentheses = {}
        # for i in range(len(string)):
        #     stack_pop = stack.pop()
        #
        #     if stack_pop == "(" or stack_pop == ")":
        #         parentheses[len(string) - i] = stack_pop


case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

# parentheses_checker(case1)
# parentheses_checker(case2)
# parentheses_checker(case3)
parentheses_checker(case4)
# parentheses_checker(case5)
# parentheses_checker(case6)