from itertools import permutations, combinations

date = ['A','B','C','D','E']
result = list(permutations(date,2))
print(result)

result2 = list(combinations(date,2))
print(result2)


# 그외 heapq, bisect, collections 는 아직 안함