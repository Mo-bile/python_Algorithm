from collections import Counter

def solution(participant, completion):
    
    remaining = Counter(participant) - Counter(completion)
    # print(list(remaining.keys())[0])
    answer = str(list(remaining.keys())[0])
    return answer
#     ps = Counter(participant)
#     cs = Counter(completion)
    
#     for p in ps:
#         if p in cs:
#             ps[p] -= 1
    
#     for k, v in ps.items():
#         if v != 0 :
#             return k