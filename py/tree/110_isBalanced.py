# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    110. 平衡二叉树
    给定一个二叉树，判断它是否是高度平衡的二叉树。
    本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
    """
    def isBalanced(self, root: TreeNode) -> bool:
        # 思路：递归，设计个方法，不是平衡树就返回-1，是平衡树就返回树的高度;
        # 平衡树需要满足条件，左右子树都是平衡树，且左右子树高度差不超过1
        return self.check(root) != -1

    def check(self, root: TreeNode) -> int:
        # 1. root为[]时
        if not root: return 0

        # 2. 考虑左子树
        l = self.check(root.left) # 已涵盖root.left == None的情况
        # 左子树不是平衡树的情况
        if l == -1: return -1

        # 3. 考虑右子树
        r = self.check(root.right) # 已涵盖root.right == None的情况
        # 右子树不是平衡树的情况
        if r == -1: return -1

        # 4. 考虑左右子树高度差大于1的情况
        if abs(l-r) > 1: return -1

        # 5. 返回数的高度
        return max(l, r) + 1
        
        
        