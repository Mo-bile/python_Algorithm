def solution(phone_book):
    phone_book.sort()
    result = True
    
    # for phone in phone_book:
    #     for phone_v in phone_book:
    #         if (phone != phone_v) and (len(phone) < len(phone_v)):
    #             return phone_v.startswith(phone)
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False            
                
    return result