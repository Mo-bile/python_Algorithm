from heapify_code import *

class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)  # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1) # 삽입된 노드(추가된 데이터)의 위치를 재배치

    def extract_max(self):
        """최우선순위 데이터 추출 메소드"""

        # 1. root노드와 마지막 노드 위치 바꾸기
        swap(self.heap, 1, len(self.heap) - 1)

        # 2. 마지막 위치로 간 root 노드 데이터 별도 변수 저장, 노드 힙에서 제거
        root_node = self.heap.pop()

        # 3. 새로운 root 노드 대상으로 히피파이 하여 힙속성 복원
        heapify(self.heap, 1, len(self.heap))

        # 4. 리턴
        return root_node

    def __str__(self):
        return str(self.heap)

# 출력 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())