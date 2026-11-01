# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #root = [1,2,3,4,5,6,7]
        res = []

        q = collections.deque()
        q.append(root) #Started with q = [1]
        
        while q:
            qLen = len(q) #len = 1
            level = []
            for i in range(qLen):
                node = q.popleft() # q=[]
                if node:
                    level.append(node.val) #level = [1]
                    q.append(node.left)  #q=[2]
                    q.append(node.right) #q=[2,3]
            if level:
                res.append(level)
        return res

