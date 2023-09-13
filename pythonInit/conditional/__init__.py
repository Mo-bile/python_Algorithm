# in, not in 연산자
data = [i for i in range(0,101, 10)]
print(data)

# 인라인 조건문
if data in [0,10]: print("true")

# 조건부 표현식
score = 85
result = "success" if score == 85 else "false"
print(result)

# 조건부 표현식 심화
a = [i for i in range(1,5)]
a.append(3)
a.append(5)
a.append(5)
a.append(5)
print(a)

remove_set = {3,5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

# -> 간소화
b = [i for i in range(1,5)]
b.append(3)
b.append(5)
b.append(5)
b.append(5)
print(b)

result2 = [j for j in b if j not in remove_set]
print(result2)
