from collections import Counter

def solution(s):
    l = s.lower()
    counter = Counter(l)
    
    if counter['p'] == counter['y']:
        return True
    else :
        return False

    