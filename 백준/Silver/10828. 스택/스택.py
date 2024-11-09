import sys

def sysPrint(s):
    sys.stdout.write(str(s) + "\n")
N = int(sys.stdin.readline())

stack = list()

for _ in range(N):
    sysInput = list(sys.stdin.readline().split())
    opp = sysInput[0]

    if opp == "push":
        stack.append(sysInput[1])
    elif opp == "pop":
        if len(stack) == 0 :
            sysPrint(-1)
            continue
        sysPrint(stack.pop())
    elif opp == "size":
        sysPrint(len(stack))
    elif opp == "empty":
        if len(stack) == 0 :
            sysPrint(1)
        else:
            sysPrint(0)
    elif opp == "top":
        if len(stack) == 0 :
            sysPrint(-1)
            continue
        sysPrint(stack[-1])
    else:
        sysPrint("error")