import sys

# N, M 입력
N, M = sys.stdin.readline().split()
a_dict = {}
b_count = {}
count = 0
# N 입력
for i in range(int(N)):
    T, S, *a = sys.stdin.readline().split()
    a = "".join(a)[:3]

    if a in a_dict:
        a_dict[a].append(S)
    else :
        a_dict[a] = [S]


# M 입력
for j in range(int(M)):
    b_list = sys.stdin.readline().split()
    b = "".join(b_list)

    if b in a_dict:
        if len(a_dict[b]) > 1:
            print("?")
        else :
            print(a_dict[b][0])
    else :
        print("!")