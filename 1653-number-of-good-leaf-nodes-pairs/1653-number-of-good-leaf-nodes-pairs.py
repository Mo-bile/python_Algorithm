# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#         def inorder(root, leaf_list):
#             if root:
#                 inorder(root.left, leaf_list)
#                 if root.left is None and root.right is None:
#                     leaf_list.append(root)
#                 inorder(root.right, leaf_list)
#             return leaf_list
#         def dfs(root, leaf_list):
#             # visited = set()
#             distances = -1
#             stack = leaf_list
#             while stack:
#                 leaf = stack.pop()
#         leaf_list = []
#         leaf_list = inorder(root, leaf_list)
#         dfs(root, leaf_list)

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right  : # falsy 처럼 조회
                return [1]

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1
            
            current_distances = [d + 1 for d in left_distances + right_distances if d + 1 <= distance]
            print(current_distances)

            return current_distances

        self.result = 0
        dfs(root)

        return self.result