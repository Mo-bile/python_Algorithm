def solution(sizes):
    big, small = [], []
    
    for size in sizes:
        # for i in range(len(size)):
        big.append(max(size))
        small.append(min(size))
    
    # 큰값과 작은 값 각각 도출하기
    bob = max(big)
    sob = max(small)
    return bob * sob