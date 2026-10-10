# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # get height of left and height of right
    # if abs(left_height - right_height)  > 1 return false
        if root == None:
            return True
       
        def get_height(node):
            if node == None:
                return 0, True
            (left_height, left_is_balanced) = get_height(node.left)
            (right_height, right_is_balanced) = get_height(node.right)
            
            height = max(left_height, right_height) + 1
            is_balanced =left_is_balanced and right_is_balanced and abs(left_height-right_height) <= 1
            return (height, is_balanced)
    
        return get_height(root)[1]
       

