# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
       # compare the trees

        def sameTree(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
       
        # find subroot in root

        def findNode(node):
            if not node:
                return False

            if sameTree(node, subRoot):
                return True

            return findNode(node.left) or findNode(node.right)

        return findNode(root)



        


