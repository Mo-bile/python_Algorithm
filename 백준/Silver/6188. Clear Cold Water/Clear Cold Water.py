from collections import deque


def read_input():
    """입력을 처리하고 트리 구조를 반환하는 함수"""
    # N 파이프 갯수, C 가짓점 갯수
    N, C = map(int, input().split())

    tree = {i: [] for i in range(1, N + 1)}
    for _ in range(C):
        E_i, B1_i, B2_i = map(int, input().split())
        tree[E_i].append(B1_i)
        tree[E_i].append(B2_i)
        # 양방향 연결을 위해 추가
        tree[B1_i].append(E_i)
        tree[B2_i].append(E_i)

    return N, tree

def calculate_distances(N, tree):
    """BFS 또는 DFS를 사용하여 각 파이프의 거리를 계산하는 함수"""
    distances = [-1] * (N + 1) # 인덱스 1부터 사용하기 위해 N + 1크기

    queue = deque([1])
    distances[1] = 1

    while queue:
        current = queue.popleft()

        for neighbor in tree[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances

def print_distances(distances):
    """계산된 거리를 출력하는 함수"""
    for i in range(1, len(distances)):
        print(distances[i])

if __name__ == "__main__":
    # 1. 입력을 받아 트리 구조 생성
    N, tree = read_input()

    # 2. 각 파이프의 거리를 계산
    distances = calculate_distances(N, tree)

    # 3. 계산된 거리를 출력
    print_distances(distances)
