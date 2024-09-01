import sys
from  itertools import combinations

def integer_count(n,m):
    count = 0
    for combo in combinations(range(1, n),2):
        if (combo[0]**2 + combo[1]**2 + m) % (combo[0]*combo[1]) == 0:
            count += 1
    return count


T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int,sys.stdin.readline().split())
    count = integer_count(n, m)
    print(count)

