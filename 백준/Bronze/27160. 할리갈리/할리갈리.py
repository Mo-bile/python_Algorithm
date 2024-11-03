import sys

N = int(sys.stdin.readline())
dict = {}
answer = "NO"

for i in range(N):
    S = sys.stdin.readline()
    fruit, count = S.split()
    c = int(count)

    if fruit in dict:
        dict[fruit] += c
    else :
        dict[fruit] = c

for k, v in dict.items():
    if v == 5:
        answer = "YES"

print(answer)