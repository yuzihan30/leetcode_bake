# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：给定二叉树 [3,9,20,null,null,15,7]
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 思路：递归，树的最大深度=左右子树的最大深度+1
        # 1. 初始化及特殊处理
        if not root: return 0
        # 2. 递归
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1