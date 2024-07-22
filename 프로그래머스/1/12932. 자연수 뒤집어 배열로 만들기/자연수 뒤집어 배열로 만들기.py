def solution(n):
    # ten = 10
    # while(True):
    #     if n / ten == 1:
    #         break
    #     else :
    #         ten = ten * 10
    #         return ten
    answer = []
    
    
    
    size =  10 ** (len(str(n)) - 1)
    while(True):
        value =  n // size
        new_n = n % size
        answer.append(value)
        
        if size != 1:
            size = size // 10
            n = new_n
        else :
            break
        
    answer.reverse()
    
    return answer


