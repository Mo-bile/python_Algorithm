# def solution(brown, yellow):
#     answer = []
#     if brown == (yellow + 3) * 2:
#         answer.append(yellow + 2)
#         answer.append(3)
    

#     return answer

def solution(brown, yellow):
    total = brown + yellow

    for height in range(1, total + 1):
        if total % height == 0: 
            width = total // height
            if width >= height and (width - 2) * (height - 2) == yellow:
                return [width, height] 