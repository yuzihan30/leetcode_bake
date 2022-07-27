# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    101. 对称二叉树
    给你一个二叉树的根节点 root ， 检查它是否轴对称。
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 思路：递归，注意是左右子树对称，而非左右子树相等
        return self.check(root.left, root.right)
        
    # 校验两个根节点，对应的二叉树是否轴对称的方法
    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        # 左右都是空
        if not left and not right: return True
        # 左或者右为空，或者左值不等于右值
        if not left or not right or left.val != right.val: return False
        # 递归判断左根节点的左子树，和右根节点的右子树是否轴对称；
        # 递归判断右根节点的左子树，和左根节点的右子树是否轴对称
        return self.check(left.left, right.right) and self.check(left.right, right.left)

