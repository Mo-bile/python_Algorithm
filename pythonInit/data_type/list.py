a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[4])

# 초기화 방법 2가지
b = list()
print(b)

c = []
print(c)

# 크기가 N 인 1차원리스트 초기화
n = 10
a = [0] * n
print(a)

a.clear()
print("클리어")
print(a)
# 인덱싱, 슬라이싱


# 초기회
for i in range(1,10):
    a.append(i)
print(a)

# 인덱싱 : 특정 인덱스로 원소접근
print(a[3])
print(a[-1])
# 슬라이싱 : 연속적인 위치 가지는 원소접근
print(a[5:9])

# 리스트 컨프리헨션
array = [i for i in range(20) if i % 2 == 1]
print(array)

    # 위 리스트 초기화 코드 컨프리헨션으로 바꾸기
array2 = [i for i in range(1,10)]
print(array2)

# 2차원 리스트 초기화에 유용
# 3 X 4 초기화
n = 3
m = 4

# '_' 는 반복 변수값 불필요 일시
array3 = [[0] * m for _ in range(n)]
print(array3)

# insert( O(1) ) append( O(NlogN) ) remove( O(N) ) 주의



