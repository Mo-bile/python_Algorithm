class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # output = [[0] * numRows]
        output = [[0] * (i + 1) for i in range(numRows)]
        
        for i in range(numRows):
            output[i][0] = 1
            output[i][-1] = 1

            for j in range(1,i):
                if j != 0 or j != i:
                    output[i][j] = output[i-1][j-1] + output[i-1][j] 
        
        return output
        