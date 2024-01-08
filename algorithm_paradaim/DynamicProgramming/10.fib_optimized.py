def fib_optimized(n):
    previous = 0
    current = 1
    temp = 0
    for i in range(1, n):
        temp = current
        current += previous
        previous = temp

    return current

# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
