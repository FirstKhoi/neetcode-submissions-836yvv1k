class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def BST(root2, target2):
            if not root2:
                return False
            if root2.val == target2:
                return True
            elif root2.val > target2:
                return BST(root2.left, target2)
            else:
                return BST(root2.right, target2)
        
        def dfs(root, target):
            if not root:
                return False
            if BST(root2, target - root.val):
                return True
            return dfs(root.left, target) or dfs(root.right, target)
            
        return dfs(root1, target)