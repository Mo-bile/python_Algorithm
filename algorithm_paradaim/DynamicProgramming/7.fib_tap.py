def fib_tab(n):
    fib_table = dict()
    fib_table[0] = 1
    fib_table[1] = 1
    for i in range(2, n):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n - 1]

# 테스트 코드
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))