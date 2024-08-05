def solution(answers):
    first, second, third = [], [], []

    first_pattern = [1, 2, 3, 4, 5]
    second_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    third_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    i = 0
    f = 0
    s = 0
    t = 0
    while len(answers) > i:
        first.append(first_pattern[f])
        if len(first_pattern) -1 > f:
            f += 1
        else:
            f = 0

        second.append(second_pattern[s])
        if len(second_pattern) -1 > s:
            s += 1
        else:
            s = 0

        third.append(third_pattern[t])
        if len(third_pattern) -1 > t:
            t += 1
        else:
            t = 0
        i += 1

    correct_f = 0
    correct_s = 0
    correct_t = 0
    for i in range(len(answers) ):
        if first[i] == answers[i]:
            correct_f += 1
        if second[i] == answers[i]:
            correct_s += 1
        if third[i] == answers[i]:
            correct_t += 1

    answer = []
    max_value = max(correct_f,correct_s,correct_t)
    if max_value == correct_f:
        answer.append(1)
    if max_value == correct_s:
        answer.append(2)
    if max_value == correct_t:
        answer.append(3)
    return answer