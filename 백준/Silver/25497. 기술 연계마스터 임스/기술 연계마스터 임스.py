import sys

N = int(sys.stdin.readline())
count = 0

values = list(sys.stdin.readline())
# has_L = False
# has_S = False
buffer = []
i = 0
while i < N :
    value = values[i]

    if value in "123456789":
        count += 1
    elif value in "LS":
        buffer.append(value)
    elif value == "R":
        if "L" in buffer:
            buffer.remove("L")
            count += 1
        else:
            break
    elif value == "K":
        if "S" in buffer:
            buffer.remove("S")
            count += 1
        else:
            break
    else :
        break
    i += 1

sys.stdout.write(str(count))
