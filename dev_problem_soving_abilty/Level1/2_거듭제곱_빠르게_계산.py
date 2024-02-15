def power(x, y):
    x_table = list()
    #base case
    if  y < 1:
        return 1

    if y % 2 == 0 :
        return power(x, y // 2) * power(x, y // 2)
    else:
        return x * power(x, y // 2) * power(x, y // 2)


# 테스트 코드
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))