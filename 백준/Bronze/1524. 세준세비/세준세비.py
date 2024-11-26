import sys

# 1-1. 게임 횟수 입력
games = int(sys.stdin.readline())
# 1-2. 세준 N, 세비 M 명 병사 (같을 경우 세바 병사 사망)
for _ in range(games):
    sys.stdin.readline().strip()
    NM = list(map(int,sys.stdin.readline().split()))
    # 1-3. 세준 병사의 힘들, 세바 병사 들의 힘들 입력 & 정렬
    Jn_armies = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    Bm_armies = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    # 2. 게임 진행
    while Jn_armies and Bm_armies:
        if Jn_armies[-1] < Bm_armies[-1]:
            n_army = Jn_armies.pop()
        else:
            m_army = Bm_armies.pop()

    if Jn_armies:
        # sys.stdout.write("\nS")
        print("S")
    elif Bm_armies:
        # sys.stdout.write("B")
        print("B")