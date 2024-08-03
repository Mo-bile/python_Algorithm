# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     data = root

    #     while root is not None:
    #         if data == val:
    #             return self.subTree(root)
    #         elif data < val: #찾으려는 값이 더 크면 오른쪽으로
    #             return self.searchBST(root.right, val)
    #         elif data > val:
    #             return self.searchBST(root.left, val)

    #     return None

    # def subTree(self, root : Optional[TreeNode]) -> Optional[TreeNode]:
    #     data = root.val
    #     subTree_list = TreeNode(data)

    #     if data is not None:
    #         subTree_list.left = TreeNode(root.left)
    #         subTree_list.right = TreeNode(root.right)

    #     return subTree_list
            
