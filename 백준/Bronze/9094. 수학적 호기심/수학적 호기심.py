if __name__ == "__main__":

    case_number = int(input())

    case = []
    for _ in range(case_number):
        case.append(list(map(int,input().split())))

    def numerator(a, b, m):
        return a**2 + b**2 + m # 계속 ^ 이걸로 쉬프트연산으로 함


    for n, m in case:
        count = 0
        for a in range(1,n):
            for b in range(a + 1, n):
                if numerator(a,b,m) % (a*b) == 0:
                    count += 1
        print(count)