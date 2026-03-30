# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def getHeight(node):
            if node is None:
                return -1

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            currHeight = max(leftHeight, rightHeight) + 1

            if len(self.res) == currHeight:
                self.res.append([])

            self.res[currHeight].append(node.val)
            return currHeight

        getHeight(root)
        return self.res