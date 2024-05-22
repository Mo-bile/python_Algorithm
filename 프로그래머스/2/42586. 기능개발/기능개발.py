def solution(progresses, speeds):
    answer = []
    
    left_days = []
    for progress, speed in zip(progresses, speeds):    
        for i in range(100):
            left_day = progress + (i * speed)
            if left_day >= 100:
                left_days.append(i) # 변수 제대로 넣자
                break
    
    tmp = left_days[0] # 처음 것
    count = 1 
    for day in left_days[1:]:
        
        # max_value = max(day, tmp) #완료 날짜될 날짜와 앞 날짜 비교
        if day <= tmp: # 앞날짜가 여전히 더 클 때
            count += 1 
        else : # 앞 날짜가 더 적을 때
            answer.append(count)
            tmp = day
            count = 1
        
        # if day > tmp :
        #     answer.append(count)
        #     tmp = day
        #     count = 1
        # else :
        #     count += 1
    answer.append(count)

    return answer