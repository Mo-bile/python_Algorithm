import sys

N, K = map(int,(sys.stdin.readline().split()))
A = list(map(int,sys.stdin.readline().split()))
A = A[:N]
A.sort()

sys.stdout.write(str(A[K - 1]))