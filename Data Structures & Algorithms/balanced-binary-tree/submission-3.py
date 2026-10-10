# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:       # 


        
        root_height = 0 
        if not root:
            return True

        def compute_height_and_get_balanced(node: TreeNode | None):
            if not node:
                return [0, True]
            else:
                left_height, left_is_balanced = compute_height_and_get_balanced(node.left)
                right_height, right_is_balanced = compute_height_and_get_balanced(node.right)

                
               
                height = max(left_height, right_height) + 1 
                return [height, abs(left_height - right_height) <= 1 and left_is_balanced and right_is_balanced ]

        
        return compute_height_and_get_balanced(root)[1]


        