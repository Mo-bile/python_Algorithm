class Node:
    """ 링크드 리스트의 노드 클리스"""
    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스

# 데이터가 2,3,5,7,11 을 담는 노드 인스턴스들 생성
head_node =  Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드 순서대로 출력
iterator = head_node #반복문으로 리스트 볼 때 도움주는 역할

# iterator 가 none이 아닌동안 반복함
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

class LikedList:
    """ 링크드 리스트 클래스 """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None: # 링크드 리스트가 비어 있는 경우
            self.head = new_node
            self.tail = new_node
        else: # 링크드 리스트가 비어 있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

# 새로운 링크드 리스트 생성
my_list = LikedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# 링크드 리스트 출력
iterator = head_node
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

