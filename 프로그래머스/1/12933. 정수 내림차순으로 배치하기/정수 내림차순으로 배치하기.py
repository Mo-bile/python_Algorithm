def solution(n):
    list_n = list(map(int, str(n)))
    sorted_n = sorted(list_n, reverse=True)
    str_n = list(map(str,sorted_n))
    result = ''.join(str_n)
    return int(result)