def fib_memo(n, cache):
    # baseCase
    if n <= 2 :
        # return n
        return 1

    # cache[n]이 존재하지 않는 경우
    if cache.get(n) is None:
        

    # cache[n]이 존재하는 경우
    else:




def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


    # fib_memo()




# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(100))