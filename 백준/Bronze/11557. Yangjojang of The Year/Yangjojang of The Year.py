import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    univ = []
    for n in range(N):
        s, a = sys.stdin.readline().split()
        univ.append((s, int(a)))
    univ.sort(key= lambda x : x[1], reverse=True)
    sys.stdout.write(univ[0][0] + '\n')