def solution(clothes):
    answer = 0
        
    dict = {}
    for clothe in clothes:
        kind = clothe[1]
        
        # 조건문으로 분기 시켜주어야함
        if kind in dict: 
            dict[kind] += 1
        else:
            dict[kind] = 1
        
    
    comb = 1
    for count in dict.values():
        comb *= (count + 1) # 종류별 옷 선택 X 경우도 포함 + 1
    
    answer = comb - 1 # 아무것도 선택하지 않은경우 제외
        
    
    return answer