class Solution:
    # for each node in the tree, we will maintain three values
    class State:
        def __init__(self, nodes, sum_val, max_average):
            self.node_count = nodes
            self.value_sum = sum_val
            self.max_average = max_average

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        return self.max_average(root).max_average

    def max_average(self, root):
        if root is None:
            return self.State(0, 0, 0)


        left = self.max_average(root.left)
        right = self.max_average(root.right)

        node_count = left.node_count + right.node_count + 1
        sum_val = left.value_sum + right.value_sum + root.val
        max_average = max(
            (1.0 * sum_val) / node_count,  
            max(right.max_average, left.max_average)
        )

        return self.State(node_count, sum_val, max_average)