import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        heap = []
        answer = [""] * len(score)

        for i in range(len(score)):
            heapq.heappush(heap, (-score[i],i))
        
        # i = 0
        # for h in (heap) :
            # poped_tuple = h
        for i in range(len(score)):
            poped_tuple = heapq.heappop(heap)

            if i == 0:
                answer[poped_tuple[1]] = "Gold Medal"
            elif i == 1:
                answer[poped_tuple[1]] = "Silver Medal"
            elif i == 2:
                answer[poped_tuple[1]] = "Bronze Medal"
            else:
                answer[poped_tuple[1]] = str(i + 1)
            # i += 1
            

        return answer

    

        # stroed_score = score
        # score.sort(reverse=True)
        # dic = {}

        # for i in range(len(score)):
        #     if i == 0:
        #         dic[score[i]] = "Gold Medal"
        #     elif i == 1:
        #         dic[score[i]] = "Silver Medal"
        #     elif i == 2:
        #         dic[score[i]] = "Bronze Medal"
        #     else :
        #         dic[score[i]] = str(i + 1)
        

        # return dic