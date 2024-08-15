class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        common_value = set(edges[0])
        
        for edge in edges[1:]:
            common_value = common_value.intersection(set(edge))
        print(common_value)

        return common_value.pop()