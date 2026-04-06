# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()

        if root:
            queue.append(root)

        res = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                if i == level_length - 1:
                    res.append(curr.val)

        return res
            

        



            

                
                
                



            
