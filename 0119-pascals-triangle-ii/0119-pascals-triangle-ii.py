class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 or rowIndex == 1 :           
            output = [1] * (rowIndex + 1)
            return output

        output = [1] * (2)
        for i in range(2, rowIndex + 1):
            newList = [1] * (i + 1)
            print(newList)

            for j in range(1,i):
                newList[j] = output[j-1] + output[j]
                print(newList)
            output = newList

        return output
            