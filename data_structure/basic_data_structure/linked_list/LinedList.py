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

print("-----------")
class LikedList:
    """ 링크드 리스트 클래스 """
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        """ 링크드 리스트 접근연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None: # 링크드 리스트가 비어 있는 경우
            self.head = new_node
            self.tail = new_node
        else: # 링크드 리스트가 비어 있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        # 하나만 있을 경우
        # if self.head is self.tail:
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        # 가장 앞 노드 선택 -> head 제거
        elif node_to_delete.prev is None:
            self.head = self.head.next
            self.head.prev = None
        # 가장 끝 노드 선택 -> tail 제거
        elif node_to_delete.next is None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.data

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        # 가장 마지막 순서 삽입
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node

        else: # 두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node

    def delete_after(self, previous_node):
        """링크드 리스트 삭제연산. 주어진 노드 뒤 노드를 삭제한다"""
        data = previous_node.next.data

        # 지우려는 노드가 tail 일때
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        # 두 노드 사이를 노드를 지울 떄
        else:
            previous_node.next = previous_node.next.next

        return data

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head

        self.head = new_node

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

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

print("-----------")
# 링크드 리스트 노드에 접근 (데이터 가지고 오기)
print(my_list.find_node_at(3).data)
# 링크드 리스트 노드에 접근 (데이터 바꾸기)
my_list.find_node_at(2).data = 13

print(my_list) # 전체 링크드 리스트 출력

print("----- 삭 제 ------")
my_list2 = LikedList()

my_list2.append(2)
my_list2.append(3)
my_list2.append(5)
my_list2.append(7)
my_list2.append(11)

print(my_list2)

node2 = my_list2.find_node_at(2)
print(my_list2.delete_after(node2))

print(my_list2)
