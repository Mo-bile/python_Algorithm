# 기본 연산
result = sum([1,2,3,45])
print(result)

result2 = min([1,4,6,4,2,1])
print(result2)

# 정렬
list = [2,5,6,1,23,57,341,533,51,65,9,4]
result3 = sorted(list, reverse=True)
print(result3)

# 튜플정렬 (key)
tuple_list = [(3,"김"), (5,"이"),(1,"박"),(9,"최")]
print(tuple_list)
tuple_list_sort= sorted(tuple_list,key = lambda x : x[1])
print(tuple_list_sort)

# 딕셔너리 정렬 안됨 -> list 로 특정 요소만 반환이 됨
dic_list = dict()
dic_list['3'] = '김'
dic_list['5'] = '이'
dic_list['1'] = '박'
dic_list['7'] = '최'
print(dic_list)
dic_list_sort = sorted(dic_list, key= lambda x : x[0])
print(type(dic_list_sort))
print(dic_list_sort)