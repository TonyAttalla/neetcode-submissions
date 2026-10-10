# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [None] * 1000
        level = 0
        q = collections.deque([])
        q.append(root)
        while len(q):  
            res[level] = []
            nodes_at_level = []
            while (len(q)):
                nodes_at_level.append(q.popleft()) 
            for node in nodes_at_level:
                res[level].append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            level +=1
        return res[0:level]
        
        
        

        