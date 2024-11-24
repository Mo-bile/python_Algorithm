class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        tuple_list = []
        # 1. 메달별 tuple 정렬
        for i in range(len(score)):
            tuple_list.append((i, score[i]))
        tuple_list.sort(key = lambda x : x[1], reverse = True)
        
        # 2. 크기만큼 미리 정렬
        output = [0 for i in range(len(score))]

        # 3. tupe 방식에 따라 재정렬
        for i in range(len(score)):
            medal = ""
            if i == 0:
                medal = "Gold Medal"
            elif i == 1:
                medal = "Silver Medal"
            elif i == 2:
                medal = "Bronze Medal"
            else:
                medal = str(i + 1)
            output[tuple_list[i][0]] = medal
        return output