# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    95. 不同的二叉搜索树 II
    给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
    """
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 思路： 三层循环递归法，将问题转化成[1,n]区间内，经过某个点分割的左右子树
        # 1. 初始化及特殊处理
        # if n == 1: return [[1]] # 易错点
        if n == 1: return [TreeNode(1)] # 也可以不写，因为后续的过程已包含这个特殊情况
        # 2. 返回结果值
        return self.buildTree(1, n)

    # 定义构建二叉搜索树的递归方法
    def buildTree(self, l: int, r: int) -> List[Optional[TreeNode]]:
        # 初始化及特殊处理
        if l > r: return [None] # 需要注意的地方，这里返回单个None构成的数组
        ans = [] # 不同二叉搜索数的集合
        # 三层遍历，外层遍历n个节点, 递归构建左右子树
        for i in range(l, r+1):
            leftTrees = self.buildTree(l, i-1)
            rightTrees = self.buildTree(i+1, r)
            m, n = len(leftTrees), len(rightTrees)
            # 从leftTrees中选一个左子树
            for j in range(m):
                # 从rightTrees中选一个右子树
                for k in range(n):
                    # 构建二叉树
                    root = TreeNode(i)
                    root.left = leftTrees[j]
                    root.right = rightTrees[k]
                    ans.append(root)
        # 返回结果值
        return ans # 易漏点

