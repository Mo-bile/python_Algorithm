class Solution:
    def largestInteger(self, num: int) -> int:

        str_num = str(num)
        # 1. 홀수 짝수 자릿수 찾기
        bigger = "even" if int(str_num[0]) % 2 == 0 else "odd"
        even_num_seat = [i for i in range(len(str_num)) if int(str_num[i]) % 2 == 0]  #짝수
        odd_num_seat = [i for i in range(len(str_num)) if int(str_num[i]) % 2 == 1] # 홀수

        # print(even_num_seat)
        # print(odd_num_seat)

        # 2. 자릿수의 수 중에 수 정렬하기
        even_num, odd_num = [], []
        for seat in even_num_seat:
            even_num.append(int(str_num[seat]))
        for seat in odd_num_seat:
            odd_num.append(int(str_num[seat]))
        even_num.sort()
        odd_num.sort()
        # print(even_num)
        # print(odd_num)

        # 3. 생성 후 처리하기
        output = [0 for i in range(len(str_num))]
        for v in even_num_seat:
            output[v] = even_num.pop()
        for v in odd_num_seat:
            output[v] = odd_num.pop()
        # print(output)
        return int(''.join(list(map(str, output))))

    # 짝수홀수 자릿수로 잘못 이해함
        # 1. 짝수 홀수 분리
        # str_num = str(num)
        # even_num = [int(str_num[i]) for i in range(0,len(str_num), 2)] #짝수
        # odd_num = [int(str_num[i]) for i in range(1,len(str_num), 2)] # 홀수

        # odd_num.sort(reverse = True)
        # even_num.sort(reverse = True)

        # print(odd_num)
        # print(even_num)

        # output = []
        # for i in range(len(str_num)):
        #     if i % 2 == 1: #홀수
        #         output.append(odd_num[i // 2])
        #     elif i % 2 == 0: #짝수
        #         output.append(even_num[i // 2])
        # return int(''.join(list(map(str, output))))