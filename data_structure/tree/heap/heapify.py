def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    # print("tree_size is ",tree_size)
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 여기에 코드를 작성하세요
    # 1. 3가지 값 중 가장 큰 값은?
    max_value = max(tree[index], tree[left_child_index], tree[right_child_index])

    # 2. 부모라면 그대로, 자식이라면 위치 바꾸기
    max_index = tree.index(max_value)
    # print(max_index)
    if tree[index] != max_value:
        swap(tree, index, max_index)

    # 3. 다음 인덱스로 이동 (자식)
    if(max_index * 2 < tree_size + 1):
        heapify(tree, max_index, tree_size)


# 테스트 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)