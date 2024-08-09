def solution(k, m, score):
    # k == 사과의 최대점수
    # m == 한개 상자에 사과의 수
    # score == 사과의 점수들
    
    score.sort()
    
    price = 0
    apple_box = []
    # while m - 1 < len(score) :
    while 0 < len(score)  :
        apple_box.append(score.pop())
        if len(apple_box) == m:
            price += min(apple_box) * m
            apple_box = []
    return price