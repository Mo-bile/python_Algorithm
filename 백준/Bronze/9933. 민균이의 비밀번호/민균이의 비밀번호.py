import sys
from collections import defaultdict

N = int(sys.stdin.readline())
pws_dict = defaultdict(str)
answer = ""

for _ in range(N):
    s = sys.stdin.readline().strip()
    if len(s) % 2 == 0 :
        continue
    pws_dict[s] = s[::-1]

for k in pws_dict.keys():
    if pws_dict[k] in pws_dict:
        answer = k

sys.stdout.write(str(len(answer)))
sys.stdout.write(" "+answer[len(answer)//2])