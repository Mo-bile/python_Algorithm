# key 해당 value 보다 뒤에 남은 인자의 갯수비교

def solution(citations):       
    # 1. 정렬
    citations.sort(reverse = True)
    h = 0
    # 2. 현재 citation 의 값과 자기 포함 뒤에 남은 것보다 큰지 비교
    for i, c in enumerate(citations):
        # 2-1 크다면 answer 에 담고, 다음인덱스로 이동
        if c >= i + 1:
            h = i + 1
        else :
            break
    return h