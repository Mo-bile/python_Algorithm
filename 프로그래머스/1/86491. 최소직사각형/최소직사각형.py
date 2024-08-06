def solution(sizes):
    big, small = [], []
    
    for size in sizes:
        for i in range(len(size)):
            big.append(max(size))
            small.append(min(size))
            
    
    bob = max(big)
    
    sob = max(small)
    
    
    answer = bob * sob
            
    
    return answer