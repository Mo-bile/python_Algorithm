# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder_tree(root, list):
            if root is not None:
                inorder_tree(root.left, list)
                # list.append(root.val) #node 값이 아니라 node 자체
                list.append(root)
                inorder_tree(root.right, list)
            return list
        
        nodes = inorder_tree(root,[]) 

        # 새로운 트리의 더미 루트 노드 생성
        dummy = TreeNode(0)
        current = dummy
        
        for node in nodes:
            node.left = None  # 왼쪽 자식 제거
            current.right = node  # 오른쪽 자식으로 설정
            current = node  # current를 갱신

        return dummy.right

        # list.sort(reverse = True) #리스트 정렬 생략
        # print(list)

        # 새로 생성 X
        # new_root = TreeNode()
        # new_root.val = list.pop()
        # print(root)

        # def right_tree(root: TreeNode, list) -> TreeNode:
        #     if root is None:
        #         return None
        #     # print(root)
        #     if root is not None:
        #         # print(root)
        #         # 왼쪽
        #         root.left = None
        #         # root 값
        #         root.val = list.pop()
        #         # 오른쪽
        #         # new_root = TreeNode()
        #         root.right = right_tree(root, list)
        #     return root
        
        # print(root, list)
        # return right_tree(root, list)