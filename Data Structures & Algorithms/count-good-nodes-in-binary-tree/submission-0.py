# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        # max_for_path = None
        def dfs(node, max_for_path):
            if node == None:
                return (None, max_for_path)
            if max_for_path == None or node.val >= max_for_path:
                max_for_path = node.val
                self.good_nodes +=1
            dfs(node.left, max_for_path)
            dfs(node.right, max_for_path)

        dfs(root, root.val)
        return self.good_nodes
           

        