import sys
N = int(sys.stdin.readline())
for _ in range(N):
    words = sys.stdin.readline().split()
    reverse_words = words[::-1]
    answer = " ".join(reverse_words)
    sys.stdout.write("Case #" + str(_+1) +": " + answer + "\n")