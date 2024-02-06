def power(x, y):
    #base case
    if  y < 1:
        return 1

    #recursive case
    x *= power(x , y - 2)

    return x

# 테스트 코드
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))