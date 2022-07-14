# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    102. 二叉树的层序遍历
    给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 思路：双指针加while遍历，curr_level指向当前层次节点的列表，
        # next_level指向下一层次节点列表
        # 1. 初始化及特殊处理
        if not root:
            return []
        curr_level = [root]
        res = []

        # 2. 循环遍历
        while curr_level:
            helper_list = []
            next_level = []
            for node in curr_level:
                helper_list.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(helper_list)
            curr_level = next_level
        
        # 3. 返回结果值
        return res