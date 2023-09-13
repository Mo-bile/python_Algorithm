def add(a,b):
    return a + b

print('함수의 결과: ',add(3,8))

# global

q = 0
def func():
    global q
    q += 5

for i in range(10):
    func()

print(q)


# 람다 익스프레션
result = (lambda a, b : a + b)(3,7)
print(result)

list = [i for i in range(1,50)]
print(list)


sorted_false_ = (lambda a: sorted(a,None,False))(list)
print(sorted_false_)