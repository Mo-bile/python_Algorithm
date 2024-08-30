class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    # DP 방법 -> 점화식
        output = 0
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        i = 2
        while i < len(cost) :
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            i += 1

        output = min(dp[len(cost) - 1], dp[len(cost) - 2])
        return output
        
    # 그리디 방법
        # 최소 비용 찾기
        # total, i, = 0, (len(cost))
        # while i >= 2:
        #     if cost[i - 2] <= cost[i - 1]: # 뒤쪽이 더 크면
        #         i -= 2 # 앞에 인덱스로
        #     elif cost[i - 2] > cost[i - 1]: # 앞쪽이 더 크면
        #         i -= 1
        #     print(i)
        #     total += cost[i]

        # return total