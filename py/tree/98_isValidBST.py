# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    98. 验证二叉搜索树
    给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
    有效 二叉搜索树定义如下：
    节点的左子树只包含 小于 当前节点的数。
    节点的右子树只包含 大于 当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    """
    # 初始化lastValue, 用于存储深度优先遍历过程中，当前二叉树的最大值（即右子节点的值）
    def __init__(self, lastValue=float('-inf')):
        self.lastValue = lastValue
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 思路：递归，利用中序遍历是递增序列的特点，不断递归左子树和右子树，
        # 并记录当前遍历的二叉树右子节点的值，也就是当前遍历的最大值
        # 1. 初始化及特殊处理
        # 考虑深度优先搜索子树为空的情况
        if not root: return True

        # 2. 考查左子树, 当左子树不满足二叉搜索树的条件时
        # 左子树满足二叉搜索树条件时，内部会自动更新self.lastValue值
        if not self.isValidBST(root.left): return False

        # 3. 考查当前根节点，当根节点的值不大于self.lastValue时，不满足条件
        if root.val <= self.lastValue: return False
        # 当根节点的值大于self.lastValue时， 更新lastValue值
        self.lastValue = root.val

        # 4. 考查右子树
        return self.isValidBST(root.right)

