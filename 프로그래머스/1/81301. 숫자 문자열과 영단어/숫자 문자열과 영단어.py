def solution(s):
    dict = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9" }
    result = ""
    word = ""
    
    for i, c in enumerate(s):
        if c.isdigit() : #숫자라면
            # print(c)
            result += c
            continue
        else : # 문자라면
            word += c
            # print(c)
            # print(word)
            if word in dict:
                # print(dict[word])
                result += dict[word]
                word = ""
    return int(result)


# 1. 이 문제는 운이좋겠도 인덱스와 숫자가 동일해서 list로 해도 충분이 가능함
# 2. replace()로 충분히 가능함
