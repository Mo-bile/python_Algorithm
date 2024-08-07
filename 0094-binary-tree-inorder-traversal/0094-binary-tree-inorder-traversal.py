# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ⊙ 전위 순회(preorder traverse) : 뿌리(root)를 먼저 방문
# ⊙ 중위 순회(inorder traverse) : 왼쪽 하위 트리를 방문 후 뿌리(root)를 방문
# ⊙ 후위 순회(postorder traverse) : 하위 트리 모두 방문 후 뿌리(root)를 방문

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def inorder(root, list):
            if root:
                inorder(root.left,list)
                output.append(root.val)
                inorder(root.right,list)
            return output

        # if not root:
        #     return None
        
        return inorder(root,output)


        
        