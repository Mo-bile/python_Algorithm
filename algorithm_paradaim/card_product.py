# 24
# 32
# 28

def max_product(left_cards, right_cards):
    # max = 0
    product = left_cards[0] * right_cards[0]
    for left_card in left_cards:
        for right_card in right_cards:

            # max() 로 아래 3줄코드를 모두 해결이 가능함
            product = max(product, left_card * right_card)
            # max() 를 쓰지 않은 경우
            # result = left_card * right_card
            # if(result > max):
            #     max = result
    return product



# 여기에 코드를 작성하세요

# 테스트 코드
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))