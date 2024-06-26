def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index:  # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다


# mo's solution
# def heapsort(tree):
#     """힙 정렬 함수"""
#     tree_size = len(tree) # 15
#
#     # 여기에 코드를 작성하세요
#     # 1. 리스트를 힙으로 만듬
#     for i in range(tree_size):
#         index = tree_size - i
#         heapify(tree, index, tree_size)
#
#     # 4. 힙에 남아엤는 노드 없도록 2 ~ 3 반복
#     for j in range(tree_size):
#         size_j = tree_size - j - 1
#         # 3. 새로운 root노드가 힙 속성 지키게 heapify 함
#         for i in range(tree_size):
#             # 2. root 노드와 마지막 노드 위치 바꿈 -> 힙에서 없어졌다고 가정
#             if(size_j < 1):
#                 return
#             swap(tree, 1, size_j)
#             index = tree_size - i
#             heapify(tree, index, size_j)

# 모범답안
def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    # 마지막 인덱스부터 처음 인덱스까지 heapify를 호출한다
    for index in range(tree_size-1, 0, -1):
        heapify(tree, index, tree_size)

    # 마지막 인덱스부터 처음 인덱스까지
    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i)  # root 노드와 마지막 인덱스를 바꿔준 후
        heapify(tree, 1, i)  # root 노드에 heapify를 호출한다

# 이중 for 문 이유
# 1. range() 에 대한 이유가 부족했음
# range(start, stop, step)



# 테스트 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)