from collections import deque
""""문제 : 서비스 센터 문의 처리"""

class CustomerComplaint:
    """고객 센터 문의를 나타내는 클래스"""
    def __init__(self, name, email, content):
        self.name = name
        self.email = email
        self.content = content


class CustomerServiceCenter:
    """고조선 호텔 서비스 센터 클래스"""
    def __init__(self):
        self.queue = deque()  # 대기 중인 문의를 저장할 큐 생성

    def process_complaint(self):
        """접수된 고객 센터 문의 내용 처리하는 메소드"""
        if len(self.queue) == 0 :
            print("더 이상 대기 중인 문의가 없습니다!")
            return

        complaint = self.queue.popleft()
        print("{0}님의 {1} 문의 내용 접수 되었습니다. 담당자가 배정되면 {2}로 연락드리겠습니다!"
              .format(complaint.name, complaint.content, complaint.email))
        # print(f"{complaint.name}님의 {complaint.content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {complaint.email}로 연락드리겠습니다!")

    def add_complaint(self, name, email, content):
        """새로운 문의를 큐에 추가 시켜주는 메소드"""
        self.queue.append(CustomerComplaint(name,email,content))


# 고객 문의 센터 인스턴스 생성
center = CustomerServiceCenter()

# 문의 접수한다
center.add_complaint("강영훈", "younghoon@codeit.com", "음식이 너무 맛이 없어요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()

# 문의 세 개를 더 접수한다
center.add_complaint("이윤수", "yoonsoo@codeit.kr", "에어컨이 안 들어와요...")
center.add_complaint("손동욱", "dongwook@codeit.us", "결제가 제대로 안 되는 거 같군요")
center.add_complaint("김현승", "hyunseung@codeit.ca", "방을 교체해주세요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()