# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find node n s.t n>p and n>q
        # finds LCA in node for p,q
        # 3, 4, root = 5
        #  node = 5 
        min_val = min(p.val,q.val)
        max_val = max(p.val,q.val)
        if min_val != p.val:
            p,q = q,p
        def dfs(node: TreeNode) -> TreeNode: 
            if node.val >= p.val and node.val <= q.val:
                return node
            else:
                if node.val >= q.val:
                    return dfs(node.left)
                # node.val less than p.val
                else:
                    return dfs(node.right)

        return dfs(root)




        