# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # map level to nodes
        res = defaultdict(list)
        def bfs(node, current_level):
            if node:
                res[current_level].append(node.val)
                bfs(node.left, current_level+1)
                bfs(node.right, current_level+1)

        bfs(root,0)
        result_arr = []
        for val in res.values():
            result_arr.append(val)
        return result_arr
        