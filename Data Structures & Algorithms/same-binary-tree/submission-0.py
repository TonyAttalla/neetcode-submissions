# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            print(node)
            if not node:
                print("returning empty")
                return [-101]
            return [node.val] + dfs(node.left) + dfs(node.right)
        
        tree1 = dfs(p)
        tree2 = dfs(q)   
      
        if len(tree1) != len(tree2):
            return False
        for i,elem in enumerate(tree1):
            if tree2[i] != elem:
                return False
        return True

        